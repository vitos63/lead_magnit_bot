from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from bot.keyboards.questions import QUESTIONS_KEYBOARD
from bot.keyboards.review import PERSONAL_REVIEW, REVIEW_KEYBOARD, SKIP_REVIEW
from database import SessionLocal
from models import User
from models.enums import Stage
from services.user import UserService

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    async with SessionLocal() as session:
        user = await UserService(session).get_or_add(
            User(tg_id=message.from_user.id, username=message.from_user.username)
        )
    keyboard = REVIEW_KEYBOARD if user.stage == Stage.GET_RESULT else QUESTIONS_KEYBOARD
    await message.answer("Привет!", reply_markup=keyboard)


@router.callback_query(F.data.in_({PERSONAL_REVIEW, SKIP_REVIEW}))
async def review(callback: CallbackQuery) -> None:
    await callback.answer("Скоро здесь появится следующий шаг")
