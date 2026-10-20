from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from core.settings import settings

OFFERS_BUTTON = InlineKeyboardButton(
    text="Знаю проблему. Хочу решение →", web_app=WebAppInfo(url=f"{settings.WEBAPP_URL}?screen=offers")
)

REVIEW_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Хочу личный разбор →", web_app=WebAppInfo(url=f"{settings.WEBAPP_URL}?screen=pre_questionnaire")
            )
        ],
        [OFFERS_BUTTON],
    ]
)

OFFERS_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[[OFFERS_BUTTON]])
