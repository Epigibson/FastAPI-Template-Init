from datetime import datetime
from typing import List, Optional
from uuid import UUID
from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class RoleCreate(BaseModel):
    name: str = Field(..., max_length=255)
    description: str = Field(..., max_length=255)
    permissions: List[PydanticObjectId] = Field(...)

    class Config:
        orm_mode = True


class RolOut(BaseModel):
    role_id: UUID
    name: str
    description: str
    permissions: List[PydanticObjectId]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class RoleUpdate(BaseModel):
    name: Optional[str] = Field(max_length=255)
    description: Optional[str] = Field(max_length=255)
    permissions: Optional[List[PydanticObjectId]] = Field()

    class Config:
        orm_mode = True
