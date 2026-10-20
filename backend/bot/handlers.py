from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.keyboards.admin import ADMIN_KEYBOARD
from bot.texts.start import START_MESSAGES
from core.database import SessionLocal
from core.settings import settings
from models import User
from services.user import UserService

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    async with SessionLocal() as session:
        service = UserService(session)
        user = await service.get_or_add(User(tg_id=message.from_user.id, username=message.from_user.username))
        text, keyboard = START_MESSAGES[user.stage]
        sent = await message.answer(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
        await service.set_start_message_id(user.tg_id, sent.message_id)


@router.message(Command("admin"), F.from_user.id == settings.ADMIN_TG_ID)
async def admin(message: Message) -> None:
    await message.answer("Админ-панель", reply_markup=ADMIN_KEYBOARD)
