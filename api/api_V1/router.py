from fastapi import APIRouter
from api.api_V1.handlers import usuario_handler
from api.api_V1.handlers import configurations_handler
from api.api_V1.handlers import notificaciones_handler
from api.api_V1.handlers import todo_handler
from api.api_V1.handlers import role_handler
from api.api_V1.handlers import permission_handler
from api.auth.jwt import auth_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth', tags=["Auth"])
router.include_router(usuario_handler.user_router, prefix='/user')
router.include_router(configurations_handler.configuraciones_router, prefix='/configuration')
router.include_router(notificaciones_handler.notification_router, prefix='/notification')
router.include_router(todo_handler.todo_router, prefix='/todo', tags=["Todo"])
router.include_router(role_handler.role_router, prefix='/role')
router.include_router(permission_handler.permission_router, prefix='/permission')
