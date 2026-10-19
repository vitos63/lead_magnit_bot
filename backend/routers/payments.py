from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from schemas.payments import (
    PRODUCTS,
    PaymentCreate,
    PaymentLink,
    PaymentStatus,
    Product,
    ProductInfo,
    YooKassaNotification,
)
from services.payment import PaymentService

router = APIRouter(prefix="/payments")


@router.get("/products")
async def get_products() -> dict[Product, ProductInfo]:
    return PRODUCTS


@router.post("")
async def create_payment(item: PaymentCreate, session: AsyncSession = Depends(get_session)) -> PaymentLink:
    return await PaymentService(session).create(item)


@router.get("/{payment_id}")
async def get_payment_status(payment_id: str, session: AsyncSession = Depends(get_session)) -> PaymentStatus:
    return PaymentStatus(status=await PaymentService(session).sync(payment_id))


@router.post("/webhook")
async def payment_webhook(notification: YooKassaNotification, session: AsyncSession = Depends(get_session)) -> None:
    await PaymentService(session).sync(notification.object.id)
