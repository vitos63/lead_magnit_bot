from bot.keyboards.web_app import web_app_keyboard
from models.enums import Stage

RESULT_KEYBOARD = web_app_keyboard("Посмотреть персональное решение →")

RESULT_KEYBOARDS = {
    Stage.GET_RESULT: RESULT_KEYBOARD,
    Stage.OPEN_PRE_QUESTIONNAIRE: web_app_keyboard("Продолжить анкету →"),
}
