from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

PERSONAL_REVIEW = "personal_review"
SKIP_REVIEW = "skip_review"

REVIEW_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Личный разбор", callback_data=PERSONAL_REVIEW),
            InlineKeyboardButton(text="Пропуск разбора", callback_data=SKIP_REVIEW),
        ]
    ]
)
