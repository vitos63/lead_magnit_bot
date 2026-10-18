from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from core.settings import settings

QUESTIONS_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Ответить на вопросы", web_app=WebAppInfo(url=settings.WEBAPP_URL))]]
)
