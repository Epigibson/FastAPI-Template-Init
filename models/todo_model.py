from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field

from models.user_model import Usuario


class Todo(Document):
    todo_id: UUID = Field(default_factory=uuid4, unique=True)
    estatus: bool = False
    titulo: Indexed(str)
    descripcion: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[Usuario]

    def __repr__(self) -> str:
        return f"<Todo {self.titulo}>"

    def __str__(self) -> str:
        return self.titulo

    def __hash__(self) -> int:
        return hash(self.titulo)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Todo):
            return self.todo_id == other.todo_id
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name= "Todo"