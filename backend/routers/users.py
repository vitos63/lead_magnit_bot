from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from schemas.user import UserOut
from services.user import UserService

router = APIRouter(prefix="/users")


@router.get("/{tg_id}")
async def get_user(tg_id: int, session: AsyncSession = Depends(get_session)) -> UserOut:
    user = await UserService(session).get(tg_id)
    if not user:
        raise HTTPException(status_code=404)
    return user
