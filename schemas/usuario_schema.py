from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, constr


class UsuarioAuth(BaseModel):
    email: EmailStr = Field(..., description="Email de Usuario")
    username: str = Field(..., min_length=5, max_length=50, description="Nombre de Usuario")
    password: str = Field(..., min_length=6, max_length=10, description="Contraseña del Usuario")


class UsuarioOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    hashed_password: str
    telefono: Optional[str]
    movil: Optional[int]
    fecha_nacimiento: Optional[str]
    estatus: Optional[bool]


class UsuarioUpdate(BaseModel):
    email: Optional[EmailStr] = Field(description="Email de Usuario")
    telefono: Optional[constr(min_length=6, max_length=12, regex="^[0-9]+$")]
    movil: Optional[int]
    fecha_nacimiento: Optional[str]
    estatus: Optional[bool]
