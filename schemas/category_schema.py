from datetime import datetime
from typing import Optional, List
from uuid import UUID
from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    category_name: str = Field(unique=True)
    category_description: str = Field(default="")
    category_image: Optional[str] = Field(default=None)
    related_products: Optional[List[PydanticObjectId]] = Field(default=[])


class CategoryOut(BaseModel):
    category_id: UUID
    category_name: str
    category_description: str
    category_image: Optional[str]
    related_products: Optional[List[PydanticObjectId]]
    status: bool
    created_at: datetime
    updated_at: datetime


class CategoryUpdate(BaseModel):
    category_description: Optional[str] = Field()
    category_image: Optional[str] = Field()
    related_products: Optional[List[PydanticObjectId]] = Field()
    status: Optional[bool] = Field()
    updated_at: datetime = Field(default_factory=datetime.utcnow)
