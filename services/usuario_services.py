from typing import Optional, List
from uuid import UUID
import pymongo.errors
from core.security import get_password, verify_password
from models.role_model import Role
from models.user_model import Usuario
from models.veterianrian_info_model import VeterinarianInfo
from schemas.usuario_schema import UsuarioAuth, UsuarioUpdate


class UsuarioService:
    @staticmethod
    async def create_usuario(usuario: UsuarioAuth):
        user_in = Usuario(
            username=usuario.username,
            email=usuario.email,
            hashed_password=get_password(usuario.password),
            role=usuario.role,
            name=usuario.name,
            user_type=usuario.user_type,
        )
        await user_in.insert()

        if user_in.user_type == "veterinarian":
            veterinarian = VeterinarianInfo(
                user=user_in.id,
                name=usuario.name,
                email=usuario.email,
            )
            await veterinarian.insert()
            user_in.additional_data = veterinarian.id
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
        if usuario:
            role = await Role.find_one(Role.id == usuario.role)
            if role:
                usuario.role = role.name
        return usuario

    @staticmethod
    async def get_all_usuarios() -> List[Usuario]:
        usuarios = await Usuario.find_all().to_list()
        # Primero Verificamos que hay usuarios
        if usuarios:
            # Iteramos cada usuario en la lista que obtenemos
            for usuario in usuarios:
                # Obtenemos el rol mediante una consulta pasandole el ID
                role = await Role.find_one(Role.id == usuario.role)
                # Verificamos si se encontro el rol
                if role:
                    # Asignamos el valor del nombre al rol en lugar del ID
                    usuario.role = role.name
        return usuarios

    @staticmethod
    async def get_usuario_by_id(id: UUID) -> Optional[Usuario]:
        usuario = await Usuario.find_one(Usuario.user_id == id)
        if usuario:
            role = await Role.find_one(Role.id == usuario.role)
            if role:
                usuario.role = role.name
        return usuario

    @staticmethod
    async def update_user(id: UUID, data: UsuarioUpdate) -> Usuario:
        usuario = await Usuario.find_one(Usuario.user_id == id)
        if not usuario:
            raise pymongo.errors.OperationFailure("Usuario no encontrado")
        await usuario.update({"$set": data.dict(exclude_unset=True)})
        return usuario
