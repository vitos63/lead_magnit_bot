from enum import Enum

from pydantic import BaseModel


class Product(str, Enum):
    GENERATOR = "generator"
    MASTER_GROUP = "master_group"


class ProductInfo(BaseModel):
    title: str
    price: int
    old_price: int


PRODUCTS = {
    Product.GENERATOR: ProductInfo(title="AI-интенсив «Генератор продаж»", price=2999, old_price=15000),
    Product.MASTER_GROUP: ProductInfo(title="Мастер-группа «Система заявок на органике»", price=24500, old_price=49000),
}


class PaymentCreate(BaseModel):
    tg_id: int
    product: Product


class PaymentLink(BaseModel):
    url: str


class YooKassaConfirmation(BaseModel):
    confirmation_url: str


class YooKassaPayment(BaseModel):
    id: str
    status: str
    confirmation: YooKassaConfirmation | None = None


class YooKassaNotification(BaseModel):
    object: YooKassaPayment
