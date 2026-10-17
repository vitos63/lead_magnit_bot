from enum import Enum

from pydantic import BaseModel


class Question(str, Enum):
    HAS_PRODUCT = "has_product"
    PRODUCT_DESCRIPTION = "product_description"
    TEN_SECONDS = "ten_seconds"
    HAS_OFFER = "has_offer"
    OFFER_DESCRIPTION = "offer_description"
    CHANNELS = "channels"
    MAIN_CHANNEL = "main_channel"
    TRIES = "tries"
    THIRTY = "thirty"
    HAS_NEXT_STEP = "has_next_step"
    PIN_POST = "pin_post"
    CLIENT_MUST_TO_DO = "client_must_to_do"


QUESTION_TEXTS = {
    Question.HAS_PRODUCT: "У вас есть конкретный продукт или услуга с понятным результатом, стоимостью и форматом работы?",
    Question.PRODUCT_DESCRIPTION: "Что именно вы сейчас продаёте? Опишите продукт, для кого он и какой результат получает клиент.",
    Question.TEN_SECONDS: (
        "Может ли новый человек за 10 секунд понять, какую проблему решает ваш продукт "
        "и почему стоит обратиться именно к вам?"
    ),
    Question.HAS_OFFER: "Есть ли у вас конкретное предложение, которое вы регулярно озвучиваете потенциальным клиентам?",
    Question.OFFER_DESCRIPTION: (
        "Напишите ваше текущее предложение клиенту так, как вы обычно формулируете его в посте или переписке."
    ),
    Question.CHANNELS: (
        "Из каких каналов привлекаете холодную целевую аудиторию? "
        "Есть ли органические каналы привода целевой аудитории (бесплатные)?"
    ),
    Question.MAIN_CHANNEL: "Есть ли у вас один основной канал, из которого вы регулярно привлекаете новую аудиторию?",
    Question.TRIES: "Что вы уже пробовали для привлечения новых людей?",
    Question.THIRTY: "Понятно ли новому посетителю вашего Telegram-канала за 30 секунд, кому вы помогаете и что предлагаете?",
    Question.HAS_NEXT_STEP: (
        "Есть ли в Telegram понятный следующий шаг: написать вам, оставить заявку, пройти диагностику "
        "или записаться на консультацию?"
    ),
    Question.PIN_POST: (
        "Есть ли у вас закреплённый пост или другой понятный маршрут, который знакомит нового подписчика с вами, "
        "продуктом и результатами клиентов?"
    ),
    Question.CLIENT_MUST_TO_DO: (
        "Представьте, что потенциальный клиент заинтересовался вашим контентом. "
        "Что конкретно он должен сделать дальше, чтобы стать вашим клиентом?"
    ),
}
LAST_QUESTION = list(Question)[-1]


class QuestionAnswer(BaseModel):
    tg_id: int
    question: Question
    answer: bool | str


class Scores(BaseModel):
    product: int
    offer: int
    traffic: int
    telegram: int


class ResultText(BaseModel):
    text: str
