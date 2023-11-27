from datetime import datetime
from typing import Optional
from uuid import UUID
from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    product_name: str = Field()
    product_description: str = Field()
    quantity_stock: int = Field()
    category: PydanticObjectId = Field()
    brand: str = Field()
    price: float = Field()
    is_active: bool = Field(default=True)
    images: Optional[list[str]] = Field()
    sizes: Optional[list[str]] = Field()
    ingredients: Optional[list[str]] = Field()
    comments_reviews: Optional[list[str]] = Field()
    labels_tags: Optional[list[str]] = Field()


class ProductOut(BaseModel):
    product_id: UUID
    product_name: str
    product_description: str
    quantity_stock: int
    category: PydanticObjectId
    brand: str
    price: float
    seller: PydanticObjectId
    is_active: bool
    images: Optional[list[str]]
    sizes: Optional[list[str]]
    ingredients: Optional[list[str]]
    comments_reviews: Optional[list[str]]
    labels_tags: Optional[list[str]]
    created_at: datetime
    updated_at: datetime


class ProductUpdate(BaseModel):
    product_name: Optional[str] = Field()
    product_description: Optional[str] = Field()
    quantity_stock: Optional[int] = Field()
    category: Optional[PydanticObjectId] = Field()
    brand: Optional[str] = Field()
    price: Optional[float] = Field()
    is_active: Optional[bool] = Field()
    images: Optional[list[str]] = Field()
    sizes: Optional[list[str]] = Field()
    ingredients: Optional[list[str]] = Field()
    comments_reviews: Optional[list[str]] = Field()
    labels_tags: Optional[list[str]] = Field()
    updated_at: datetime = Field(default_factory=datetime.utcnow)
