from typing import List
from uuid import UUID
import pymongo.errors
from fastapi import APIRouter, HTTPException, status, Depends
from api.deps.user_deps import get_current_user
from models.user_model import Usuario
from schemas.usuario_schema import UsuarioAuth, UsuarioOut, UsuarioUpdate
from services.usuario_services import UsuarioService

user_router = APIRouter()


@user_router.post('/create', summary="Crear nuevo usuario", response_model=UsuarioOut)
async def create_user(data: UsuarioAuth):
    try:
        usuario = await UsuarioService.create_usuario(data)
        return usuario

    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario con este Username o correo electronico ya existe"
        )


@user_router.put('/update', summary="Actualizar usuario")
async def update_user(data: UsuarioUpdate, usuario: Usuario = Depends(get_current_user)):
    try:
        return await UsuarioService.update_user(usuario.user_id, data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario que deseas actualizar no existe"
        )


@user_router.get('/me', summary="Se obtiene el usuario logeado", response_model=UsuarioOut)
async def get_me(usuario: Usuario = Depends(get_current_user)):
    try:
        return usuario
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no esta logeado"
        )


@user_router.get('/list', summary='Se obtiene un listado de todos los Usuarios', response_model=List[UsuarioOut])
async def list_usuarios():
    try:
        result = UsuarioService.get_all_usuarios()
        return await result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se encontraron registros"
        )


@user_router.put('update/admin/{user_id}', summary='Se actrualiza el usuario seleccionandolo mediante el ID',
                 response_model=UsuarioOut)
async def update_user_as_admin(user_id: UUID, data: UsuarioUpdate):
    try:
        result = UsuarioService.update_user(user_id, data)
        return await result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo editar el registro"
        )
