from uuid import UUID

from models.permission_model import Permission
from models.role_model import Role
from schemas.role_schema import RoleCreate, RoleUpdate


class RoleService:

    @staticmethod
    async def create(data: RoleCreate):
        result = Role(**data.dict())
        await result.insert()
        return result

    @staticmethod
    async def retrieve(role_id: UUID):
        result = await Role.find_one(Role.role_id == role_id)
        if result:
            permissions = result.permissions
            permissions_data = []
            if permissions:
                for item in permissions:
                    permission = await Permission.find_one(Permission.id == item)
                    permissions_data.append(permission.name)
            result.permissions = permissions_data
        return result

    @staticmethod
    async def retrieve_name(role_name: str):
        result = await Role.find_one(Role.name == role_name)
        return result

    @staticmethod
    async def list():
        roles = await Role.find_all().to_list()
        if roles:
            for role in roles:
                permissions = role.permissions
                permissions_data = []
                if permissions:
                    for item in permissions:
                        permission = await Permission.find_one(Permission.id == item)
                        permissions_data.append(permission.name)
                role.permissions = permissions_data
        return roles

    @staticmethod
    async def update(role_id: UUID, data: RoleUpdate):
        result = await RoleService.retrieve(role_id)
        await result.update({"$set": data.dict(exclude_unset=True)})
        result.commit()
        return result

    @staticmethod
    async def delete(role_id: UUID):
        result = await RoleService.retrieve(role_id)
        await result.delete()
        message = f"Role {role_id} deleted successfully"
        return message
