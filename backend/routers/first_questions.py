from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from schemas.first_questions import LAST_QUESTION, Question, QuestionAnswer, ResultText
from services.first_questions import FirstQuestionsService

router = APIRouter(prefix="/first_questions")


@router.post("")
async def receive_answer(
    item: QuestionAnswer, background_tasks: BackgroundTasks, session: AsyncSession = Depends(get_session)
) -> QuestionAnswer:
    service = FirstQuestionsService(session)
    await service.save_answer(item)
    if item.question == LAST_QUESTION:
        answers = await service.format_answers(item.tg_id)
        background_tasks.add_task(service.send_result, item.tg_id, answers)
    return item


@router.get("/{tg_id}")
async def get_answers(tg_id: int, session: AsyncSession = Depends(get_session)) -> dict[Question, bool | str]:
    return await FirstQuestionsService(session).get_answers(tg_id)


@router.get("/{tg_id}/result")
async def get_result(tg_id: int, session: AsyncSession = Depends(get_session)) -> ResultText:
    text = await FirstQuestionsService(session).get_result(tg_id)
    if not text:
        raise HTTPException(status_code=404)
    return ResultText(text=text)
