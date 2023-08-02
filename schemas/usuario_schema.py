from typing import Optional
from uuid import UUID

from beanie import Link, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field, constr

from models.role_model import Role


class UsuarioAuth(BaseModel):
    email: EmailStr = Field(..., description="Email de Usuario")
    username: str = Field(..., min_length=5, max_length=50, description="Nombre de Usuario")
    password: str = Field(..., min_length=6, max_length=10, description="Contraseña del Usuario")
    role: Optional[PydanticObjectId]


class UsuarioOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    hashed_password: str
    role: Optional[PydanticObjectId]
    phone: Optional[int]
    mobile: Optional[int]
    birthday: Optional[str]
    status: Optional[bool]


class UsuarioUpdate(BaseModel):
    email: Optional[EmailStr] = Field(description="Email de Usuario")
    role: Optional[PydanticObjectId]
    phone: Optional[int]
    mobile: Optional[int]
    birthday: Optional[str]
    status: Optional[bool]
