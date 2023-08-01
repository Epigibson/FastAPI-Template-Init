from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class ConfiguracionesCreate(BaseModel):
    correos_notificaciones: Optional[list] = Field()


class ConfiguracionOut(BaseModel):
    configuracion_id: UUID
    notificaciones: Optional[bool]
    correos_notificaciones: Optional[list]


class ConfiguracionUpdate(BaseModel):
    notificaciones: Optional[bool] = Field(default=True)
    correos_notificaciones: Optional[list] = Field()

