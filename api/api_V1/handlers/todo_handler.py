from typing import List
from uuid import UUID
import pymongo.errors
from fastapi import APIRouter, HTTPException, status, Depends
from api.deps.user_deps import get_current_user
from models.todo_model import Todo
from models.user_model import Usuario
from schemas.todo_schema import TodoOut, TodoCreate, TodoUpdate
from services.todo_services import TodoService

todo_router = APIRouter()

@todo_router.get('/', summary="Traer todos los datos de Usuario", response_model=List[TodoOut])
async def listado(current_user : Usuario = Depends(get_current_user)):
    try:
        result = TodoService.list_todos(current_user)
        return await result
    except pymongo.errors.OperationFailure:
        result_error = TodoService.list_todos(current_user)
        if result_error is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No se encontraron registros del usuario"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error, usuario no encontrado"
            )

@todo_router.post('/create', summary="Creacion de registros de usuario", response_model=Todo)
async def create_todo(data: TodoCreate, current_user: Usuario = Depends(get_current_user)):
    try:
        return await TodoService.create_todo(current_user, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se ha podido crear el registro del Usuario"
        )

@todo_router.get('/{todo_id}', summary="Obtener registros de Usuario", response_model=TodoOut)
async def retrieve(todo_id: UUID, current_user : Usuario = Depends(get_current_user)):
    try:
        return await TodoService.retrieve_todo(current_user, todo_id)
    except pymongo.errors.InvalidDocument:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontro el registro"
        )

@todo_router.put('/{todo_id}', summary="Editar registro de usuario", response_model=TodoOut)
async def update(todo_id: UUID, data: TodoUpdate, current_user: Usuario = Depends(get_current_user)):
    try:
        return await TodoService.update_todo(current_user, todo_id, data)
    except pymongo.errors.InvalidDocument:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo actualizar el registro"
        )

@todo_router.delete('/{todo_id}', summary="Eliminar un registro de usuario")
async def delete_todo(todo_id: UUID, current_user: Usuario = Depends(get_current_user)):
    try:
        return await TodoService.delete_todo(current_user, todo_id)
    except pymongo.errors.InvalidDocument:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se econtro el registro especificado"
        )
