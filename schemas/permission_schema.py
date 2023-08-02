from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class PermissionCreate(BaseModel):
    name: str = Field(..., max_length=255)
    description: str = Field(..., max_length=255)

    class Config:
        orm_mode = True


class PermissionOut(BaseModel):
    permission_id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PermissionUpdate(BaseModel):
    name: Optional[str] = Field(max_length=255)
    description: Optional[str] = Field(max_length=255)

    class Config:
        orm_mode = True
