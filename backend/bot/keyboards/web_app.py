from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from core.settings import settings


def web_app_keyboard(text: str, screen: str | None = None) -> InlineKeyboardMarkup:
    url = f"{settings.WEBAPP_URL}?screen={screen}" if screen else settings.WEBAPP_URL
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, web_app=WebAppInfo(url=url))]])
