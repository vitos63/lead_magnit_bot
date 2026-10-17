from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.questions import QUESTIONS_KEYBOARD
from database import SessionLocal
from models import User
from services.user import UserService

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    async with SessionLocal() as session:
        await UserService(session).add_if_not_exists(
            User(tg_id=message.from_user.id, username=message.from_user.username)
        )
    await message.answer("Привет!", reply_markup=QUESTIONS_KEYBOARD)
