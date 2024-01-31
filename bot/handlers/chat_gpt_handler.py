import openai
from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.chat_action import ChatActionSender
from telegram import constants
from telegram.constants import ParseMode

from bot.database.main import firebase
from bot.database.models.common import Quota, Currency, Model
from bot.database.models.transaction import ServiceType, TransactionType
from bot.database.models.user import UserSettings, User
from bot.database.operations.chat import get_chat
from bot.database.operations.message import write_message, get_messages_by_chat_id
from bot.database.operations.role import get_role_by_name
from bot.database.operations.transaction import write_transaction
from bot.database.operations.user import get_user, update_user
from bot.helpers.create_new_message_and_update_user import create_new_message_and_update_user
from bot.helpers.reply_with_voice import reply_with_voice
from bot.helpers.send_message_to_admins import send_message_to_admins
from bot.integrations.openAI import get_response_message
from bot.keyboards.chat_gpt import build_chat_gpt_continue_generating_keyboard
from bot.keyboards.common import build_recommendations_keyboard
from bot.locales.main import get_localization

chat_gpt_router = Router()

PRICE_GPT3_INPUT = 0.000001
PRICE_GPT3_OUTPUT = 0.000002
PRICE_GPT4_INPUT = 0.00001
PRICE_GPT4_OUTPUT = 0.00003


@chat_gpt_router.message(Command("chatgpt3"))
async def chatgpt3(message: Message, state: FSMContext):
    await state.clear()

    user = await get_user(str(message.from_user.id))

    if user.current_model == Model.GPT3:
        reply_markup = await build_recommendations_keyboard(user)
        await message.answer(
            text=get_localization(user.language_code).ALREADY_SWITCHED_TO_THIS_MODEL,
            reply_markup=reply_markup,
        )
    else:
        user.current_model = Model.GPT3
        await update_user(user.id, {
            "current_model": user.current_model,
        })

        reply_markup = await build_recommendations_keyboard(user)
        await message.answer(
            text=get_localization(user.language_code).SWITCHED_TO_CHATGPT3,
            reply_markup=reply_markup,
        )


@chat_gpt_router.message(Command("chatgpt4"))
async def chatgpt4(message: Message, state: FSMContext):
    await state.clear()

    user = await get_user(str(message.from_user.id))

    if user.current_model == Model.GPT4:
        reply_markup = await build_recommendations_keyboard(user)
        await message.answer(
            text=get_localization(user.language_code).ALREADY_SWITCHED_TO_THIS_MODEL,
            reply_markup=reply_markup,
        )
    else:
        user.current_model = Model.GPT4
        await update_user(user.id, {
            "current_model": user.current_model,
        })

        reply_markup = await build_recommendations_keyboard(user)
        await message.answer(
            text=get_localization(user.language_code).SWITCHED_TO_CHATGPT4,
            reply_markup=reply_markup,
        )


async def handle_chatgpt(message: Message, state: FSMContext, user: User, user_quota: Quota):
    user_data = await state.get_data()

    text = user_data.get('recognized_text', None)
    if text is None:
        text = message.text

    await write_message(user.current_chat_id, "user", user.id, text)

    chat = await get_chat(user.current_chat_id)
    messages = await get_messages_by_chat_id(user.current_chat_id)
    role = await get_role_by_name(chat.role)
    sorted_messages = sorted(messages, key=lambda m: m.created_at)
    history = [
                  {
                      'role': 'system',
                      'content': role.translated_instructions.get(user.language_code, 'en')
                  }
              ] + [
                  {
                      'role': message.sender,
                      'content': message.content
                  } for message in sorted_messages
              ]

    processing_message = await message.reply(text=get_localization(user.language_code).processing_request_text())

    if user.settings[user.current_model][UserSettings.TURN_ON_VOICE_MESSAGES]:
        chat_action_sender = ChatActionSender.record_voice
    else:
        chat_action_sender = ChatActionSender.typing

    async with chat_action_sender(bot=message.bot, chat_id=message.chat.id):
        try:
            response = await get_response_message(user.current_model, history)
            response_message = response['message']
            if user_quota == Quota.GPT3:
                service = ServiceType.GPT3
                input_price = response['input_tokens'] * PRICE_GPT3_INPUT
                output_price = response['output_tokens'] * PRICE_GPT3_OUTPUT
            elif user_quota == Quota.GPT4:
                service = ServiceType.GPT4
                input_price = response['input_tokens'] * PRICE_GPT4_INPUT
                output_price = response['output_tokens'] * PRICE_GPT4_OUTPUT
            else:
                raise NotImplemented

            total_price = round(input_price + output_price, 6)
            message_role, message_content = response_message.role, response_message.content
            await write_transaction(user_id=user.id,
                                    type=TransactionType.EXPENSE,
                                    service=service,
                                    amount=total_price,
                                    currency=Currency.USD,
                                    quantity=1,
                                    details={
                                        "input_tokens": response['input_tokens'],
                                        "output_tokens": response['output_tokens'],
                                        "request": text,
                                        "answer": message_content,
                                    })

            transaction = firebase.db.transaction()
            await create_new_message_and_update_user(transaction, message_role, message_content, user, user_quota)

            if user.settings[user.current_model][UserSettings.TURN_ON_VOICE_MESSAGES]:
                reply_markup = build_chat_gpt_continue_generating_keyboard(user.language_code)
                await reply_with_voice(message=message,
                                       text=message_content,
                                       user_id=user.id,
                                       reply_markup=reply_markup if response['finish_reason'] == 'length' else None)
            else:
                chat_info = f'💬 {chat.title}\n' if (
                    user.settings[user.current_model][UserSettings.SHOW_THE_NAME_OF_THE_CHATS]
                ) else ''
                role_info = f'{role.translated_names.get(user.language_code, "en")}\n' if (
                    user.settings[user.current_model][UserSettings.SHOW_THE_NAME_OF_THE_ROLES]
                ) else ''
                header_text = f'{chat_info}{role_info}\n' if chat_info or role_info else ''
                footer_text = f'\n\n✉️ {user.monthly_limits[user_quota] + user.additional_usage_quota[user_quota] + 1}' \
                    if user.settings[user.current_model][UserSettings.SHOW_USAGE_QUOTA] else ''
                reply_markup = build_chat_gpt_continue_generating_keyboard(user.language_code)
                try:
                    await message.reply(
                        f"{header_text}{message_content}{footer_text}",
                        reply_markup=reply_markup if response['finish_reason'] == 'length' else None,
                        parse_mode=ParseMode.MARKDOWN,
                    )
                except TelegramBadRequest as e:
                    if "can't parse entities" in str(e):
                        await message.reply(
                            f"{header_text}{message_content}{footer_text}",
                            reply_markup=reply_markup if response['finish_reason'] == 'length' else None,
                            parse_mode=None,
                        )
                    else:
                        raise
        except openai.BadRequestError as e:
            if e.code == 'content_policy_violation':
                await message.reply(
                    text=get_localization(user.language_code).REQUEST_FORBIDDEN_ERROR,
                )
        except Exception as e:
            await message.answer(
                text=get_localization(user.language_code).ERROR,
                parse_mode=None
            )
            await send_message_to_admins(bot=message.bot,
                                         message=f"#error\n\nALARM! Ошибка у пользователя при запросе в ChatGPT: {user.id}\n"
                                                 f"Информация:\n{e}",
                                         parse_mode=None)
        finally:
            await processing_message.delete()


@chat_gpt_router.callback_query(lambda c: c.data.startswith('chat_gpt:'))
async def handle_chat_gpt_choose_selection(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    user = await get_user(str(callback_query.from_user.id))

    action = callback_query.data.split(':')[1]

    if action == 'continue_generating':
        await state.update_data(recognized_text=get_localization(user.language_code).CONTINUE_GENERATING)
        if user.current_model == Model.GPT3:
            user_quota = Quota.GPT3
        elif user.current_model == Model.GPT4:
            user_quota = Quota.GPT4
        else:
            raise NotImplemented

        await handle_chatgpt(callback_query.message, state, user, user_quota)
        await callback_query.message.edit_reply_markup(reply_markup=None)

    await state.clear()
