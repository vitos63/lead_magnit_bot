from schemas.first_questions import Diagnosis, Direction, Result, Scores

DIRECTIONS = {
    "product": "Продукт",
    "offer": "Оффер",
    "traffic": "Трафик",
    "telegram": "Telegram",
}

LEAK_TEXTS = {
    "product": "Вы умеете работать. Но клиенту непонятно, что именно покупать.",
    "offer": "Продукт есть. Но зачем его покупать — непонятно.",
    "traffic": "Ваш продукт готов к продажам. Но новых людей приходит недостаточно.",
    "telegram": "Вы привели человека в канал. А дальше отправили его на экскурсию по постам.",
}

DIAGNOSES = {
    "product": Diagnosis(
        title="Вы эксперт. А что у вас покупать?",
        paragraphs=[
            "У вас есть опыт, знания и результаты. Но клиент не понимает, за что именно должен заплатить.",
            "Ваша экспертность пока не упакована в понятную коммерческую ценность.",
        ],
        recommendation=(
            "Определить конкретный результат работы с вами, собрать понятный продукт, обозначить формат "
            "и ценность для клиента."
        ),
    ),
    "offer": Diagnosis(
        title="Продукт есть. Причина купить — нет.",
        paragraphs=[
            "Клиенту всё равно, сколько консультаций входит в вашу программу. Ему важно, что изменится в его жизни "
            "после работы с вами.",
            "Пока вы продаёте процесс, клиент не видит ценность результата.",
        ],
        recommendation=(
            "Усилить предложение, связать продукт с конкретной проблемой аудитории и объяснить, почему клиенту "
            "стоит обратиться к вам."
        ),
    ),
    "traffic": Diagnosis(
        title="Сарафан работает. Пока вас рекомендуют.",
        paragraphs=[
            "Вы можете быть прекрасным специалистом, но если новые люди о вас не узнают, количество заявок "
            "останется непредсказуемым.",
            "Прежде чем привлекать больше людей, подготовьте соцсети к их приходу.",
        ],
        recommendation=(
            "Определить подходящий канал органического привлечения холодной аудитории и выстроить понятный "
            "маршрут до заявки."
        ),
    ),
    "telegram": Diagnosis(
        title="Подписчики есть. Где заявки?",
        paragraphs=[
            "Человек зашёл, почитал и ушёл. Не потому, что вы плохой эксперт.",
            "Просто канал не объяснил, зачем ему оставаться и как у вас купить.",
            "Полезный контент без маршрута до заявки — просто бесплатная библиотека.",
        ],
        recommendation=(
            "Усилить упаковку канала, закреплённый пост и контентную воронку, которая ведёт читателя к обращению."
        ),
    ),
}


def find_leak(values: dict[str, int]) -> str:
    return min(values, key=values.get)


def format_scores(scores: Scores) -> str:
    return "; ".join(f"{DIRECTIONS[name]} — {score}/10" for name, score in scores.model_dump().items())


def build_result(scores: Scores) -> Result:
    values = scores.model_dump()
    leak = find_leak(values)
    return Result(
        directions=[Direction(title=DIRECTIONS[name], score=score) for name, score in values.items()],
        leak=DIRECTIONS[leak],
        text=LEAK_TEXTS[leak],
        diagnosis=DIAGNOSES[leak],
    )


def format_result(scores: Scores) -> str:
    values = scores.model_dump()
    leak = find_leak(values)
    return (
        f"Оценки: {format_scores(scores)}\n"
        f"ГЛАВНАЯ УТЕЧКА — {DIRECTIONS[leak].upper()} · {values[leak]}/10\n"
        f"{LEAK_TEXTS[leak]}"
    )
