from typing import Optional
from pydantic import BaseModel, Field


class VeterinarianInfoUpdate(BaseModel):
    name: Optional[str] = Field()
    specialization: Optional[str] = Field()
    years_of_experience: Optional[int] = Field()
    location: Optional[str] = Field()
    contact_number: Optional[str] = Field()
    email: Optional[str] = Field()
    website: Optional[str] = Field()
    description: Optional[str] = Field()
    profile_image: Optional[str] = Field()
    ratings_and_reviews: Optional[str] = Field()
    specialized_species: Optional[list[str]] = Field()
    languages: Optional[list[str]] = Field()
    social_media_accounts: Optional[list[str]] = Field()
    services: Optional[list[str]] = Field()
    special_services: Optional[list[str]] = Field()
