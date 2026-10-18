def format_questionnaire(texts: dict[str, str], answers: dict[str, bool | str]) -> str:
    return "\n\n".join(
        f"{number}. {text}\nОтвет: {format_answer(answers.get(question))}"
        for number, (question, text) in enumerate(texts.items(), 1)
    )


def format_answer(answer: bool | str | None) -> str | None:
    if isinstance(answer, bool):
        return "Да" if answer else "Нет"
    return answer
