from typing import Optional, List
from uuid import UUID
import pymongo.errors
from core.security import get_password, verify_password
from models.user_model import Usuario
from schemas.usuario_schema import UsuarioAuth, UsuarioUpdate


class UsuarioService:
    @staticmethod
    async def create_usuario(usuario: UsuarioAuth):
        user_in = Usuario(
            username=usuario.username,
            email=usuario.email,
            hashed_password=get_password(usuario.password),
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[Usuario]:
        user = await UsuarioService.get_usuario_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None
        return user

    @staticmethod
    async def get_usuario_by_email(email: str) -> Optional[Usuario]:
        usuario = await Usuario.find_one(Usuario.email == email)
        return usuario

    @staticmethod
    async def get_all_usuarios() -> List[Usuario]:
        usuarios = await Usuario.find_all().to_list()
        return usuarios

    @staticmethod
    async def get_usuario_by_id(id: UUID) -> Optional[Usuario]:
        usuario = await Usuario.find_one(Usuario.user_id == id)
        return usuario

    @staticmethod
    async def update_user(id: UUID, data: UsuarioUpdate) -> Usuario:
        usuario = await Usuario.find_one(Usuario.user_id == id)
        if not usuario:
            raise pymongo.errors.OperationFailure("Usuario no encontrado")
        await usuario.update({"$set": data.dict(exclude_unset=True)})
        return usuario
