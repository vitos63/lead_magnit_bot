from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from core.settings import settings

REVIEW_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Хочу личный разбор →", web_app=WebAppInfo(url=f"{settings.WEBAPP_URL}?screen=pre_questionnaire")
            )
        ]
    ]
)
