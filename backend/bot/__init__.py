from aiogram import Bot, Dispatcher

from bot.handlers import router
from settings import settings

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)
