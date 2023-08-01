from typing import List
from beanie import Document


class Notificaciones(Document):
    recipient: List[str]
    message: str

    class Settings:
        collection = "Notificaciones"
