from datetime import datetime
from typing import Optional
from uuid import UUID
from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    titulo: str = Field(..., title="Titulo", max_length=25, min_length=5)
    descripcion: str = Field(..., title="Descripcion", max_length=150, min_length=5)
    estatus: Optional[bool] = True


class TodoOut(BaseModel):
    todo_id: UUID
    estatus: bool
    titulo: str
    descripcion: Optional[str]
    owner: PydanticObjectId
    created_at: datetime
    updated_at: datetime


class TodoUpdate(BaseModel):
    titulo: Optional[str]
    descripcion: Optional[str]
    estatus: Optional[bool]
