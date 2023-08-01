from fastapi import APIRouter
from api.api_V1.handlers import usuario_handler
from api.api_V1.handlers import configuraciones_handler
from api.api_V1.handlers import notificaciones_handler
from api.api_V1.handlers import todo_handler
from api.auth.jwt import auth_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth', tags=["Auth"])
router.include_router(usuario_handler.user_router, prefix='/usuarios', tags=["Usuarios"])
router.include_router(configuraciones_handler.configuraciones_router, prefix='/configuraciones')
router.include_router(notificaciones_handler.notification_router, prefix='/notificaciones')
router.include_router(todo_handler.todo_router, prefix='/todo', tags=["Todo"])
