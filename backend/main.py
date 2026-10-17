import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from bot import bot, dp
from routers import first_questions, pre_questionnaire, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    polling = asyncio.create_task(dp.start_polling(bot, handle_signals=False))
    yield
    await dp.stop_polling()
    await polling


app = FastAPI(lifespan=lifespan)
app.include_router(first_questions.router)
app.include_router(pre_questionnaire.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app)
