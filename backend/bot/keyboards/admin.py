from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from settings import settings

ADMIN_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Открыть админку", web_app=WebAppInfo(url=f"{settings.WEBAPP_URL}?screen=admin"))]
    ]
)
