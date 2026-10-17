from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from settings import settings

SKIP_REVIEW = "skip_review"

REVIEW_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Личный разбор", web_app=WebAppInfo(url=f"{settings.WEBAPP_URL}?screen=pre_questionnaire")
            ),
            InlineKeyboardButton(text="Пропуск разбора", callback_data=SKIP_REVIEW),
        ]
    ]
)
