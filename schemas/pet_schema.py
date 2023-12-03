from datetime import datetime
from typing import Optional
from uuid import UUID

from beanie import PydanticObjectId, Link
from pydantic import BaseModel

from models.medical_history_model import MedicalHistory


class PetCreate(BaseModel):
    name: str
    profile_images: Optional[list[str]]
    nickname: str
    born_day: str
    gender: str
    color: str
    specie: str
    color_cast: str
    medical_conditions: Optional[str]
    is_adopted: Optional[bool]


class PetOut(BaseModel):
    _id: PydanticObjectId
    pet_id: UUID
    owner: PydanticObjectId
    name: str
    profile_images: Optional[list[str]]
    nickname: str
    born_day: str
    color: str
    specie: str
    color_cast: str
    medical_conditions: Optional[str]
    medical_history: Optional[Link[MedicalHistory]]
    is_active: bool
    is_adopted: bool
    created_at: datetime
    updated_at: datetime


class PetUpdate(BaseModel):
    name: Optional[str]
    profile_images: Optional[list[str]]
    nickname: Optional[str]
    born_day: Optional[str]
    gender: Optional[str]
    color: Optional[str]
    specie: Optional[str]
    color_cast: Optional[str]
    medical_conditions: Optional[str]
    is_active: Optional[bool]
    is_adopted: Optional[bool]
