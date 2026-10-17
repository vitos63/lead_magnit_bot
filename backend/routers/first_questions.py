from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from schemas.first_questions import LAST_QUESTION, QuestionAnswer
from services.first_questions import FirstQuestionsService

router = APIRouter(prefix="/first_questions")


@router.post("")
async def receive_answer(
    item: QuestionAnswer, background_tasks: BackgroundTasks, session: AsyncSession = Depends(get_session)
) -> QuestionAnswer:
    service = FirstQuestionsService(session)
    await service.save_answer(item)
    if item.question == LAST_QUESTION:
        answers = await service.get_answers(item.tg_id)
        background_tasks.add_task(service.send_result, item.tg_id, answers)
    return item
