from models import User


def format_user(user: User) -> str:
    username = f"@{user.username}" if user.username else "без username"
    return f"{username} (tg_id {user.tg_id})"


def format_review_request(user: User, result: str, answers: str) -> str:
    return f"Новая заявка на персональный разбор\nПользователь: {format_user(user)}\n\n{result}\n\nАнкета:\n\n{answers}"


def format_diagnostics(user: User, answers: str) -> str:
    return f"Ответы диагностики: {format_user(user)}\n\n{answers}"
