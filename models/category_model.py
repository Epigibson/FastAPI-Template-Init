from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, PydanticObjectId
from pydantic import Field
from typing import List, Optional


class Category(Document):
    category_id: UUID = Field(default_factory=uuid4, unique=True)
    category_name: str = Field(unique=True)
    category_description: str = Field(default="")
    category_image: Optional[str] = Field(default=None)
    related_products: Optional[List[PydanticObjectId]] = Field(default=[])
    status: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "category"
        use_state_machine = True
        use_enum_values = True
        use_fastapi_validation = True
        use_schemaless = True
        use_pydantic_get_or_create = True
        use_indexes = True
        use_uuid = True
