from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from pydantic import ValidationError

from api.deps.user_deps import get_current_user
from core.config import settings
from core.security import create_access_token, create_refresh_token
from models.user_model import Usuario
from schemas.auth_schema import TokenSchema, TokenPayload
from schemas.usuario_schema import UsuarioOut
from services.usuario_services import UsuarioService

auth_router = APIRouter()

@auth_router.post('/login', summary="Creacion de acceso y de refresco de tokens para el usuario", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UsuarioService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Correo o contraseña incorrecta"
        )

    #Crear el acceso y refrescar los tokens
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }

@auth_router.post('/test-token', summary="Prueba para verificar que el token es valido", response_model=UsuarioOut)
async def test_token(user: Usuario =  Depends(get_current_user)):
    return user

@auth_router.post('/refresh', summary="Recargar token", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token invalido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await UsuarioService.get_usuario_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Token invalido para el usuario",
        )
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }
