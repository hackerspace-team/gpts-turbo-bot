from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot.database.models.common import Model
from bot.database.operations.user import get_user, update_user
from bot.handlers.face_swap_handler import handle_face_swap
from bot.keyboards.mode import build_mode_keyboard
from bot.locales.main import get_localization

mode_router = Router()


@mode_router.message(Command("mode"))
async def mode(message: Message):
    user = await get_user(str(message.from_user.id))

    reply_markup = build_mode_keyboard(user.language_code, user.current_model)

    await message.answer(text=get_localization(user.language_code).MODE,
                         reply_markup=reply_markup)


@mode_router.callback_query(lambda c: c.data.startswith('mode:'))
async def handle_mode_selection(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    chosen_mode = callback_query.data.split(':')[1]

    keyboard = callback_query.message.reply_markup.inline_keyboard
    keyboard_changed = False

    new_keyboard = []
    for row in keyboard:
        new_row = []
        for button in row:
            text = button.text
            callback_data = button.callback_data.split(":", 1)[1]

            if callback_data == chosen_mode:
                if "✅" not in text:
                    text += " ✅"
                    keyboard_changed = True
            else:
                text = text.replace(" ✅", "")
            new_row.append(InlineKeyboardButton(text=text, callback_data=button.callback_data))
        new_keyboard.append(new_row)

    if keyboard_changed:
        await update_user(str(callback_query.from_user.id), {
            "current_model": chosen_mode
        })
        await callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(inline_keyboard=new_keyboard))

    if chosen_mode == Model.FACE_SWAP:
        await handle_face_swap(callback_query.message, state, str(callback_query.from_user.id))