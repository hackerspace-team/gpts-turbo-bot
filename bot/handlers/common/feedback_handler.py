from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.database.operations.feedback.writers import write_feedback
from bot.helpers.senders.send_message_to_admins import send_message_to_admins

from bot.keyboards.common.common import build_cancel_keyboard
from bot.locales.main import get_localization, get_user_language
from bot.states.feedback import Feedback

feedback_router = Router()


@feedback_router.message(Command("feedback"))
async def feedback(message: Message, state: FSMContext):
    await state.clear()

    user_language_code = await get_user_language(str(message.from_user.id), state.storage)

    reply_markup = build_cancel_keyboard(user_language_code)
    await message.answer(
        text=get_localization(user_language_code).FEEDBACK,
        reply_markup=reply_markup,
    )

    await state.set_state(Feedback.waiting_for_feedback)


@feedback_router.message(Feedback.waiting_for_feedback, ~F.text.startswith('/'))
async def feedback_sent(message: Message, state: FSMContext):
    user_id = str(message.from_user.id)
    user_language_code = await get_user_language(user_id, state.storage)

    await write_feedback(user_id, message.text)

    text = (f"#feedback\n\n"
            f"🚀 <b>Новая обратная связь от пользователя</b>: {user_id} 🚀\n\n"
            f"<code>{message.text}</code>")
    await send_message_to_admins(message.bot, text)

    await message.reply(text=get_localization(user_language_code).FEEDBACK_SUCCESS)

    await state.clear()


@feedback_router.callback_query(Feedback.waiting_for_feedback, lambda c: c.data == 'cancel')
async def handle_exit_selection(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    await callback_query.message.delete()

    await state.clear()
