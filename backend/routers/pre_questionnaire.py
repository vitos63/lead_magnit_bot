from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from schemas.pre_questionnaire import PreQuestion, PreQuestionAnswer
from services.pre_questionnaire import PreQuestionnaireService

router = APIRouter(prefix="/pre_questionnaire")


@router.post("")
async def receive_answer(item: PreQuestionAnswer, session: AsyncSession = Depends(get_session)) -> PreQuestionAnswer:
    await PreQuestionnaireService(session).save_answer(item)
    return item


@router.get("/{tg_id}")
async def get_answers(tg_id: int, session: AsyncSession = Depends(get_session)) -> dict[PreQuestion, bool | str]:
    return await PreQuestionnaireService(session).get_answers(tg_id)


@router.post("/{tg_id}/open")
async def open_pre_questionnaire(tg_id: int, session: AsyncSession = Depends(get_session)) -> None:
    await PreQuestionnaireService(session).open(tg_id)


@router.post("/{tg_id}/send")
async def send_pre_questionnaire(tg_id: int, session: AsyncSession = Depends(get_session)) -> None:
    await PreQuestionnaireService(session).send(tg_id)
