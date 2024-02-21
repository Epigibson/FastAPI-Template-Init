from datetime import datetime

from beanie import Document

from uuid import uuid4, UUID

from pydantic import Field


class PetImage(Document):
    pet_id: UUID = Field(...)
    pet_image_id: UUID = Field(default_factory=uuid4, unique=True)
    pet_image_name: str = Field(...)
    pet_image_url: str = Field(...)
    pet_image_type: str = Field(...)
    pet_image_size: str = Field(...)
    pet_image_extension: str = Field(...)
    pet_image_created_at: datetime = Field(default_factory=datetime.utcnow)
    pet_image_updated_at: datetime = Field(default_factory=datetime.utcnow)
    pet_image_is_avatar: bool = Field(...)
