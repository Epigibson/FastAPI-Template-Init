from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from beanie import Document, Indexed, PydanticObjectId
from pydantic import Field, EmailStr


class Usuario(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    telefono: Optional[str] = None
    movil: Optional[int] = None
    fecha_nacimiento: Optional[str]
    estatus: Optional[bool] = True


    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Usuario):
            return self.email == other.email
        return False

    @property
    def create(self, **kwargs) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_email(cls, email: str) -> "Usuario":
        return await cls.find_one(cls.email == email)

    class Config:
        orm_mode = True

    class Settings:
        collection = "Usuario"
