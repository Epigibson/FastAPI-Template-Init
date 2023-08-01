from typing import List
from pydantic import BaseModel


class NotificacionCreate(BaseModel):
    recipients: List[str]
    message: str


class NotificacionOut(BaseModel):
    recipient: List[str]
    message: str
