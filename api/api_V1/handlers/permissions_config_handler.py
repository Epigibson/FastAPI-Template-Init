
from fastapi import APIRouter, Depends, HTTPException, status
from api.deps.user_deps import get_current_user
from models.permission_model import Permission
from models.role_model import Role
from models.user_model import Usuario

permission_config_router = APIRouter()


async def validate(current_user: Usuario = Depends(get_current_user)):
    if current_user:
        role = await Role.find_one(Role.name == current_user.role)
        permissions = role.permissions
        permissions_data = []
        for item in permissions:
            permission = await Permission.find_one(Permission.id == item)
            permissions_data.append(permission.name)
        return permissions_data
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You don't have enough privileges to perform this action.",
    )
