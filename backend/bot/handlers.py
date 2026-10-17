from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.questions import QUESTIONS_KEYBOARD
from bot.keyboards.review import REVIEW_KEYBOARD
from database import SessionLocal
from models import User
from models.enums import Stage
from services.user import UserService

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    async with SessionLocal() as session:
        service = UserService(session)
        user = await service.get_or_add(User(tg_id=message.from_user.id, username=message.from_user.username))
        keyboard = QUESTIONS_KEYBOARD if user.stage == Stage.START else REVIEW_KEYBOARD
        sent = await message.answer("Привет!", reply_markup=keyboard)
        await service.set_start_message_id(user.tg_id, sent.message_id)
