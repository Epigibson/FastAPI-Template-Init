from datetime import datetime
from typing import Optional
from pydantic import Field
from uuid import UUID, uuid4
from beanie import Document, PydanticObjectId, Link, Indexed
from models.medical_history_model import MedicalHistory


class Pet(Document):
    pet_id: UUID = Field(default_factory=uuid4, unique=True)
    owner: PydanticObjectId = Field()
    name: Indexed(str)
    nickname: str = Field()
    born_day: str = Field()
    gender: str = Field()
    color: str = Field()
    specie: str = Field()
    color_cast: str = Field()
    medical_conditions: Optional[str] = Field()
    medical_history: Optional[Link[MedicalHistory]] = Field()
    is_active: bool = Field(default=True)
    is_adopted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    def __unicode__(self):
        return self.name

    class Config:
        orm_mode = True

    class Settings:
        collection = "Pet"
