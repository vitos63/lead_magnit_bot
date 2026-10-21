from pathlib import Path

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import FSInputFile, LinkPreviewOptions, Message

from bot.keyboards.admin import ADMIN_KEYBOARD
from bot.keyboards.post import POST_KEYBOARD
from bot.keyboards.result import RESULT_KEYBOARDS
from bot.texts.post import POST
from bot.texts.result import format_result
from bot.texts.start import START_MESSAGES
from core.database import SessionLocal
from core.settings import settings
from models import User
from models.enums import Stage
from repo.first_questions import FirstQuestionsRepository
from services.user import UserService

router = Router()

WELCOME_PHOTO = FSInputFile(Path(__file__).parent / "media" / "start.jpg")
POST_PREVIEW = LinkPreviewOptions(url=f"{settings.WEBAPP_URL}/post.jpg", prefer_large_media=True, show_above_text=True)


@router.message(CommandStart())
async def start(message: Message) -> None:
    async with SessionLocal() as session:
        service = UserService(session)
        user = await service.get_or_add(User(tg_id=message.from_user.id, username=message.from_user.username))
        if user.stage in START_MESSAGES:
            text, keyboard = START_MESSAGES[user.stage]
        else:
            scores = await FirstQuestionsRepository(session).get_scores(user.tg_id)
            text, keyboard = format_result(scores), RESULT_KEYBOARDS[user.stage]
        if user.stage == Stage.START:
            sent = await message.answer_photo(WELCOME_PHOTO, caption=text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
        else:
            sent = await message.answer(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
        await service.set_start_message_id(user.tg_id, sent.message_id)


@router.message(Command("admin"), F.from_user.id == settings.ADMIN_TG_ID)
async def admin(message: Message) -> None:
    await message.answer("Админ-панель", reply_markup=ADMIN_KEYBOARD)


@router.message(Command("post"), F.from_user.id == settings.ADMIN_TG_ID)
async def post(message: Message) -> None:
    await message.bot.send_message(
        settings.CHANNEL_ID, POST, reply_markup=POST_KEYBOARD, link_preview_options=POST_PREVIEW, parse_mode=ParseMode.HTML
    )
    await message.answer("Пост опубликован")
