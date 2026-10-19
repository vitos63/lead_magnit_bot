from sqlalchemy.ext.asyncio import AsyncSession

from bot import bot
from bot.texts.admin import format_purchase
from clients.yookassa import yookassa
from core.settings import settings
from models import Payment
from models.enums import Stage
from repo.payment import PaymentRepository
from repo.user import UserRepository
from schemas.payments import PRODUCTS, PaymentCreate, PaymentLink, Product


class PaymentService:
    BOT_URL = f"https://t.me/{settings.BOT_USERNAME}"

    def __init__(self, session: AsyncSession):
        self.repository = PaymentRepository(session)
        self.user_repository = UserRepository(session)

    async def create(self, item: PaymentCreate) -> PaymentLink:
        product = PRODUCTS[item.product]
        payment = await yookassa.create_payment(product.price, product.title, self.BOT_URL, {"tg_id": item.tg_id})
        await self.repository.add(
            Payment(id=payment.id, tg_id=item.tg_id, product=item.product.value, amount=product.price, status=payment.status)
        )
        return PaymentLink(id=payment.id, url=payment.confirmation.confirmation_url)

    async def sync(self, payment_id: str) -> str:
        payment = await yookassa.get_payment(payment_id)
        if await self.repository.set_status(payment_id, payment.status) and payment.status == "succeeded":
            saved = await self.repository.get(payment_id)
            await self.user_repository.advance_stage(saved.tg_id, Stage.BUY_PRODUCT)
            title = PRODUCTS[Product(saved.product)].title
            await bot.send_message(saved.tg_id, f"Оплата прошла! {title} — доступ скоро появится здесь.")
            user = await self.user_repository.get(saved.tg_id)
            await bot.send_message(settings.ADMIN_TG_ID, format_purchase(user, title, saved.amount))
        return payment.status
