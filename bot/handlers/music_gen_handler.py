from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.chat_action import ChatActionSender

from bot.database.models.common import Model, Quota
from bot.database.operations.generation import write_generation
from bot.database.operations.request import write_request, get_started_requests_by_user_id_and_model
from bot.database.operations.user import get_user, update_user
from bot.helpers.translate_text import translate_text
from bot.integrations.replicateAI import create_music_gen_melody
from bot.keyboards.common import build_recommendations_keyboard, build_cancel_keyboard
from bot.keyboards.music_gen import build_music_gen_keyboard
from bot.locales.main import get_localization
from bot.states.music_gen import MusicGen

music_gen_router = Router()

PRICE_MUSIC_GEN = 0.00115


@music_gen_router.message(Command("music_gen"))
async def music_gen(message: Message, state: FSMContext):
    await state.clear()

    user = await get_user(str(message.from_user.id))

    if user.current_model == Model.MUSIC_GEN:
        await message.answer(text=get_localization(user.language_code).ALREADY_SWITCHED_TO_THIS_MODEL)
    else:
        user.current_model = Model.MUSIC_GEN
        await update_user(user.id, {
            "current_model": user.current_model,
        })

        reply_markup = await build_recommendations_keyboard(user)
        await message.answer(
            text=get_localization(user.language_code).SWITCHED_TO_MUSIC_GEN,
            reply_markup=reply_markup,
        )

    await handle_music_gen(message.bot, str(message.chat.id), state, user.id)


async def handle_music_gen(bot: Bot, chat_id: str, state: FSMContext, user_id: str, text=None):
    user = await get_user(str(user_id))

    if text is None:
        reply_markup = await build_recommendations_keyboard(user)
        await bot.send_message(
            chat_id=chat_id,
            text=get_localization(user.language_code).MUSIC_GEN_INFO,
            reply_markup=reply_markup,
        )
    else:
        reply_markup = build_music_gen_keyboard(user.language_code)
        await bot.send_message(
            chat_id=chat_id,
            text=get_localization(user.language_code).MUSIC_GEN_TYPE_SECONDS,
            reply_markup=reply_markup,
        )

        await state.set_state(MusicGen.waiting_for_music_gen_duration)
        await state.update_data(music_gen_prompt=text)


@music_gen_router.callback_query(lambda c: c.data.startswith('music_gen:'))
async def music_gen_selection(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    duration = callback_query.data.split(':')[1]
    await handle_music_gen_selection(callback_query.message,
                                     str(callback_query.from_user.id),
                                     duration,
                                     state)


async def handle_music_gen_selection(message: Message,
                                     user_id: str,
                                     duration: str,
                                     state: FSMContext):
    user = await get_user(str(user_id))
    user_data = await state.get_data()

    processing_message = await message.reply(
        text=get_localization(user.language_code).processing_request_music_gen(),
    )

    async with ChatActionSender.record_voice(bot=message.bot, chat_id=message.chat.id):
        try:
            quota = user.monthly_limits[Quota.MUSIC_GEN] + user.additional_usage_quota[Quota.MUSIC_GEN]
            prompt = user_data['music_gen_prompt']
            duration = int(duration)

            if quota < duration:
                reply_markup = build_cancel_keyboard(user.language_code)
                await message.reply(
                    text=get_localization(user.language_code).music_gen_forbidden(quota),
                    reply_markup=reply_markup,
                )
            elif duration < 1:
                reply_markup = build_cancel_keyboard(user.language_code)
                await message.reply(
                    text=get_localization(user.language_code).MUSIC_GEN_MIN_ERROR,
                    reply_markup=reply_markup,
                )
            else:
                user_not_finished_requests = await get_started_requests_by_user_id_and_model(user.id, Model.MUSIC_GEN)

                if len(user_not_finished_requests):
                    await message.reply(
                        text=get_localization(user.language_code).ALREADY_MAKE_REQUEST,
                    )
                    await processing_message.delete()
                    return

                request = await write_request(
                    user_id=user.id,
                    message_id=processing_message.message_id,
                    model=Model.MUSIC_GEN,
                    requested=1,
                )

                if user.language_code != 'en':
                    prompt = await translate_text(prompt, user.language_code, 'en')
                result_id = await create_music_gen_melody(prompt, duration)
                await write_generation(
                    id=result_id,
                    request_id=request.id,
                    model=Model.MUSIC_GEN,
                    has_error=result_id is None,
                    details={
                        "prompt": prompt,
                        "duration": duration,
                    }
                )
        except ValueError:
            reply_markup = build_cancel_keyboard(user.language_code)
            await message.reply(
                text=get_localization(user.language_code).VALUE_ERROR,
                reply_markup=reply_markup,
            )


@music_gen_router.message(MusicGen.waiting_for_music_gen_duration, ~F.text.startswith('/'))
async def music_gen_duration_sent(message: Message, state: FSMContext):
    await handle_music_gen_selection(message, str(message.from_user.id), message.text, state)
