from typing import Optional
from uuid import UUID
from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr, Field


class UsuarioAuth(BaseModel):
    email: EmailStr = Field(..., description="Email de Usuario")
    username: str = Field(..., min_length=5, max_length=50, description="Nombre de Usuario")
    password: str = Field(..., min_length=6, max_length=25, description="Contraseña del Usuario")
    name: str = Field(..., min_length=3, max_length=50, description="Nombre del Usuario")
    role: Optional[PydanticObjectId]
    user_type: str = Field(...)


class UsuarioOut(BaseModel):
    user_id: UUID
    username: str
    name: str
    email: EmailStr
    hashed_password: str
    role: Optional[PydanticObjectId]
    phone: Optional[int]
    mobile: Optional[int]
    birthday: Optional[str]
    status: Optional[bool]
    user_type: Optional[str]
    additional_data: Optional[PydanticObjectId]


class UsuarioUpdate(BaseModel):
    email: Optional[EmailStr] = Field(description="Email de Usuario")
    name: Optional[str] = Field(description="Nombre del Usuario")
    role: Optional[PydanticObjectId]
    phone: Optional[int]
    mobile: Optional[int]
    birthday: Optional[str]
    address: Optional[str]
    status: Optional[bool]
