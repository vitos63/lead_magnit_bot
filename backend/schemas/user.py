from pydantic import BaseModel

from models.enums import Stage


class UserOut(BaseModel):
    stage: Stage
