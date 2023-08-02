from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document
from pydantic import Field


class Permission(Document):
    permission_id: UUID = Field(default_factory=uuid4, unique=True)
    name: str = Field(required=True)
    description: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __unicode__(self):
        return self.name
