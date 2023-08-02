from enum import Enum


class Role(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"


class Permission(str, Enum):
    read = 'read'
    create = 'create'
    update = 'update'
    delete = 'delete'
