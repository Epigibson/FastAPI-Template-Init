from typing import Optional
from uuid import UUID, uuid4
from beanie import Document, Link
from pydantic import Field


class Configuraciones(Document):
    configuracion_id: UUID = Field(default_factory=uuid4, unique=True)
    notificaciones: Optional[bool] = Field(default=True)
    correos_notificaciones: Optional[list] = Field(default=[])

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        collection = "Configuraciones"
