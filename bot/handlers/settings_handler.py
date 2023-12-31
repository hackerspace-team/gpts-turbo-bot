from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot.database.operations.user import get_user, update_user
from bot.keyboards.settings import build_settings_keyboard
from bot.locales.main import get_localization

settings_router = Router()


@settings_router.message(Command("settings"))
async def settings(message: Message):
    user = await get_user(str(message.from_user.id))

    reply_markup = build_settings_keyboard(user.language_code, user.settings)

    await message.answer(text=get_localization(user.language_code).SETTINGS,
                         reply_markup=reply_markup)


@settings_router.callback_query(lambda c: c.data.startswith('setting:'))
async def handle_setting_selection(callback_query: CallbackQuery):
    await callback_query.answer()

    chosen_setting = callback_query.data.split(':')[1]

    user = await get_user(str(callback_query.from_user.id))
    user.settings[chosen_setting] = not user.settings[chosen_setting]

    keyboard = callback_query.message.reply_markup.inline_keyboard

    new_keyboard = []
    for row in keyboard:
        new_row = []
        for button in row:
            text = button.text
            callback_data = button.callback_data.split(":", 1)[1]

            if callback_data == chosen_setting:
                if "✅" in text:
                    text = text.replace(" ✅", " ❌")
                else:
                    text = text.replace(" ❌", " ✅")
            new_row.append(InlineKeyboardButton(text=text, callback_data=button.callback_data))
        new_keyboard.append(new_row)

    await update_user(str(callback_query.from_user.id), {
        "settings": user.settings
    })
    await callback_query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(inline_keyboard=new_keyboard))