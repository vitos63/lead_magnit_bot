from models import User


def format_user(user: User) -> str:
    username = f"@{user.username}" if user.username else "без username"
    return f"{username} (tg_id {user.tg_id})"


def format_review_request(user: User, answers: str) -> str:
    return f"Новая заявка на личный разбор\nПользователь: {format_user(user)}\n\n{answers}"
