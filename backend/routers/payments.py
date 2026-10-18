from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from schemas.payments import PRODUCTS, PaymentCreate, PaymentLink, Product, ProductInfo, YooKassaNotification
from services.payment import PaymentService

router = APIRouter(prefix="/payments")


@router.get("/products")
async def get_products() -> dict[Product, ProductInfo]:
    return PRODUCTS


@router.post("")
async def create_payment(item: PaymentCreate, session: AsyncSession = Depends(get_session)) -> PaymentLink:
    return PaymentLink(url=await PaymentService(session).create(item))


@router.post("/webhook")
async def payment_webhook(notification: YooKassaNotification, session: AsyncSession = Depends(get_session)) -> None:
    await PaymentService(session).handle_notification(notification.object.id)
