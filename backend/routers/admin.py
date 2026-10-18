from datetime import UTC, datetime, timedelta

from aiogram.utils.web_app import safe_parse_webapp_init_data
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from schemas.admin import AdminUser, AdminUserCard
from services.admin import AdminService
from settings import settings

INIT_DATA_TTL = timedelta(days=1)


def require_admin(x_init_data: str = Header()) -> None:
    try:
        data = safe_parse_webapp_init_data(settings.BOT_TOKEN, x_init_data)
    except ValueError:
        raise HTTPException(status_code=401) from None
    if datetime.now(UTC) - data.auth_date > INIT_DATA_TTL:
        raise HTTPException(status_code=401)
    if not data.user or data.user.id != settings.ADMIN_TG_ID:
        raise HTTPException(status_code=403)


router = APIRouter(prefix="/admin", dependencies=[Depends(require_admin)])


@router.get("/users")
async def get_users(session: AsyncSession = Depends(get_session)) -> list[AdminUser]:
    return await AdminService(session).get_users()


@router.get("/users/{tg_id}")
async def get_user(tg_id: int, session: AsyncSession = Depends(get_session)) -> AdminUserCard:
    user = await AdminService(session).get_user(tg_id)
    if not user:
        raise HTTPException(status_code=404)
    return user
