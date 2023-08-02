from uuid import UUID
from models.permission_model import Permission
from schemas.permission_schema import PermissionCreate, PermissionUpdate


class PermissionServices:

    @staticmethod
    async def create(data: PermissionCreate):
        result = Permission(**data.dict())
        await result.insert()
        return result

    @staticmethod
    async def retrieve(permission_id: UUID):
        result = await Permission.find_one(Permission.permission_id == permission_id)
        return result

    @staticmethod
    async def list():
        result = await Permission.find_all().to_list()
        return result

    @staticmethod
    async def update(permission_id: UUID, data: PermissionUpdate):
        result = await PermissionServices.retrieve(permission_id)
        await result.update({"$set": data.dict(exclude_unset=True)})
        await result.save()
        return result

    @staticmethod
    async def delete(permission_id: UUID):
        result = await PermissionServices.retrieve(permission_id)
        await result.delete()
        message = f"Permission {permission_id} deleted"
        return message
