from uuid import UUID
import pymongo.errors
from fastapi import APIRouter, HTTPException, status, Depends
from api.api_V1.handlers.permissions_config_handler import validate
from api.deps.user_deps import get_current_user
from models.user_model import Usuario
from schemas.todo_schema import TodoCreate, TodoUpdate
from services.todo_services import TodoService

todo_router = APIRouter()


@todo_router.get('/', summary="Traer todos los datos de Usuario")
async def listado(user: Usuario = Depends(get_current_user)):
    try:
        result = await TodoService.list_todos(user) if "Read" in await validate(user) else None
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error, usuario no encontrado"
        )


@todo_router.post('/create', summary="Creacion de registros de usuario")
async def create_todo(data: TodoCreate, user: Usuario = Depends(get_current_user)):
    try:
        result = await TodoService.create_todo(user, data) if "Create" in await validate(user) else None
        return {f"Message": "Registry created successfully",
                "Data": result}
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se ha podido crear el registro del Usuario"
        )


@todo_router.get('/{todo_id}', summary="Obtener registros de Usuario")
async def retrieve(todo_id: UUID, user: Usuario = Depends(get_current_user)):
    try:
        result = await TodoService.retrieve_todo(user, todo_id) if "Read" in await validate(user) else None
        return result
    except pymongo.errors.InvalidDocument:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontro el registro"
        )


@todo_router.put('/{todo_id}', summary="Editar registro de usuario")
async def update(todo_id: UUID, data: TodoUpdate, user: Usuario = Depends(get_current_user)):
    try:
        return await TodoService.update_todo(user, todo_id, data) if "Update" in await validate(user) else None
    except pymongo.errors.InvalidDocument:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo actualizar el registro"
        )


@todo_router.delete('/{todo_id}', summary="Eliminar un registro de usuario")
async def delete_todo(todo_id: UUID, user: Usuario = Depends(get_current_user)):
    try:
        result = await TodoService.delete_todo(user, todo_id) if "Delete" in await validate(user) else None
        return {f"Message": f"Registry {result} deleted successfully"}
    except pymongo.errors.InvalidDocument:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se econtro el registro especificado"
        )
