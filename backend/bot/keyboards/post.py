from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from core.settings import settings

POST_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Где утекают мои заявки?", url=f"https://t.me/{settings.BOT_USERNAME}")]]
)
