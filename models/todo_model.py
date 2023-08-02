from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert, PydanticObjectId
from pydantic import Field
from models.user_model import Usuario


class Todo(Document):
    todo_id: UUID = Field(default_factory=uuid4, unique=True)
    estatus: bool = False
    titulo: Indexed(str)  # Fixed the typing declaration for Indexed
    descripcion: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: PydanticObjectId

    def commit(self):
        self.save()

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name = "Todo"
