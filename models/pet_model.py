from datetime import datetime
from typing import Optional
from pydantic import Field
from uuid import UUID, uuid4
from beanie import Document, PydanticObjectId, Link
from models.medical_history_model import MedicalHistory


class Pet(Document):
    pet_id: UUID = Field(default_factory=uuid4, unique=True)
    owner: PydanticObjectId = Field()
    name: str = Field()
    profile_images: Optional[list[str]] = Field(default=[])
    avatar_image: Optional[str] = Field()
    sterilized:  bool = Field()
    nickname: str = Field()
    born_day: str = Field()
    gender: str = Field()
    color: str = Field()
    specie: str = Field()
    color_cast: str = Field()
    medical_conditions: Optional[str] = Field()
    medical_history: Optional[Link[MedicalHistory]] = Field()
    is_active: bool = True
    is_adopted: Optional[bool] = Field()
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
