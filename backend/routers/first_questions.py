from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from schemas.first_questions import QuestionAnswer
from services.first_questions import FirstQuestionsService

router = APIRouter(prefix="/first_questions")


@router.post("")
async def receive_answer(item: QuestionAnswer, session: AsyncSession = Depends(get_session)) -> QuestionAnswer:
    await FirstQuestionsService(session).save_answer(item)
    return item
