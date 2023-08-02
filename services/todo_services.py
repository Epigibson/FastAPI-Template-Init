from typing import List
from uuid import UUID
from models.todo_model import Todo
from models.user_model import Usuario
from schemas.todo_schema import TodoCreate, TodoUpdate


class TodoService:

    @staticmethod
    async def list_todos(usuario: Usuario) -> List[Todo]:
        todos = await Todo.find(Todo.owner == usuario.id).to_list()
        for todo in todos:
            todo.owner = usuario.email
        return todos

    @staticmethod
    async def create_todo(usuario: Usuario, data: TodoCreate):
        todo = Todo(**data.dict(), owner=usuario.id)
        await todo.insert()
        return todo

    @staticmethod
    async def retrieve_todo(current_user: Usuario, todo_id: UUID):
        todo = await Todo.find_one(Todo.todo_id == todo_id, Todo.owner == current_user.id)
        if todo:
            todo.owner = current_user.email
        return todo

    @staticmethod
    async def update_todo(current_user: Usuario, todo_id: UUID, data: TodoUpdate):
        todo = await TodoService.retrieve_todo(current_user, todo_id)
        await todo.update({"$set": data.dict(exclude_unset=True)})

        await todo.save()
        return todo

    @staticmethod
    async def delete_todo(current_user: Usuario, todo_id: UUID):
        todo = await TodoService.retrieve_todo(current_user, todo_id)
        elemento: UUID = todo.todo_id
        if todo:
            await todo.delete()
        return elemento
