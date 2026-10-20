from schemas.first_questions import Direction, Result, Scores

DIRECTIONS = {
    "product": "Продукт",
    "offer": "Оффер",
    "traffic": "Трафик",
    "telegram": "Telegram",
}

LEAK_TEXTS = {
    "product": (
        "Вы умеете работать. Но клиенту непонятно, что именно покупать.\n"
        "Пока экспертность не превращена в понятный продукт, привлекать больше людей — значит "
        "приводить их к неясному предложению."
    ),
    "offer": (
        "Продукт есть. Но зачем его покупать — непонятно.\n"
        "Вы можете отлично делать свою работу. Но пока клиент не видит ценность предложения, ему "
        "проще отложить решение, чем достать карту."
    ),
    "traffic": (
        "Ваш продукт готов к продажам. Но новых людей приходит недостаточно.\n"
        "Сарафан — хороший бонус. Плохая стратегия роста."
    ),
    "telegram": (
        "Вы привели человека в канал. А дальше отправили его на экскурсию по постам.\n"
        "Если подписчик не понимает, что вы продаёте и как к вам обратиться, даже хороший контент "
        "может не довести его до заявки."
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
    )


def format_result(scores: Scores) -> str:
    values = scores.model_dump()
    leak = find_leak(values)
    return (
        f"Оценки: {format_scores(scores)}\n"
        f"ГЛАВНАЯ УТЕЧКА — {DIRECTIONS[leak].upper()} · {values[leak]}/10\n"
        f"{LEAK_TEXTS[leak]}"
    )
