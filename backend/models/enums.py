from enum import Enum


class Stage(str, Enum):
    START = "START"
    GET_RESULT = "GET_RESULT"
    OPEN_questionnaire = "OPEN_questionnaire"
    BUY_PRODUCT = "BUY_PRODUCT"
