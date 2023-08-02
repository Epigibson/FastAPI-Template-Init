from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from beanie import Document, PydanticObjectId
from pydantic import Field


class Role(Document):
    role_id: UUID = Field(default_factory=uuid4, unique=True)
    name: str = Field(required=True)
    description: str = Field(default="")
    permissions: List[PydanticObjectId] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    def __unicode__(self):
        return self.name
