from datetime import datetime
from typing import Optional
from beanie import Document, PydanticObjectId
from uuid import UUID, uuid4
from pydantic import Field


class VeterinarianInfo(Document):
    veterinarian_id: UUID = Field(default_factory=uuid4, unique=True)
    user: PydanticObjectId = Field()
    name: str = Field()
    specialization: Optional[str] = Field()
    years_of_experience: Optional[int] = Field()
    location: Optional[str] = Field()
    contact_number: Optional[str] = Field()
    email: str = Field()
    website: Optional[str] = Field()
    description: Optional[str] = Field()
    profile_image: Optional[str] = Field()
    ratings_and_reviews: Optional[str] = Field()
    specialized_species: Optional[list[str]] = Field()
    languages: Optional[list[str]] = Field()
    social_media_accounts: Optional[list[str]] = Field()
    services: Optional[list[str]] = Field()
    special_services: Optional[list[str]] = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
