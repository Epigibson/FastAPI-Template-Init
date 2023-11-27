from datetime import datetime
from typing import Optional
from beanie import Document, PydanticObjectId
from uuid import UUID, uuid4
from pydantic import Field


class Product(Document):
    product_id: UUID = Field(default_factory=uuid4, unique=True)
    product_name: str = Field()
    product_description: str = Field()
    quantity_stock: int = Field()
    category: PydanticObjectId = Field()
    brand: str = Field()
    price: float = Field()
    seller:  PydanticObjectId = Field()
    is_active: bool = Field(default=True)
    images:  Optional[list[str]] = Field()
    sizes: Optional[list[str]] = Field()
    ingredients:  Optional[list[str]] = Field()
    comments_reviews: Optional[list[str]] = Field()
    labels_tags: Optional[list[str]] = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
