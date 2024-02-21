from fastapi import APIRouter
from api.api_V1.handlers import usuario_handler
from api.api_V1.handlers import configurations_handler
from api.api_V1.handlers import notificaciones_handler
from api.api_V1.handlers import role_handler
from api.api_V1.handlers import images_serve_handler
from api.api_V1.handlers import permission_handler
from api.api_V1.handlers import pet_handler
from api.api_V1.handlers import medical_history_handler
from api.api_V1.handlers import category_handler
# from api.api_V1.handlers import product_handler
from api.api_V1.handlers import pet_images_handler
from api.auth.jwt import auth_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth', tags=["Auth"])
router.include_router(usuario_handler.user_router, prefix='/user')
router.include_router(images_serve_handler.images_serve_router, prefix='/images')
router.include_router(configurations_handler.configuraciones_router, prefix='/configuration')
router.include_router(notificaciones_handler.notification_router, prefix='/notification')
router.include_router(role_handler.role_router, prefix='/role')
router.include_router(permission_handler.permission_router, prefix='/permission')
router.include_router(pet_handler.pet_router, prefix='/pets')
router.include_router(medical_history_handler.medical_history_router, prefix='/medical_histories')
router.include_router(category_handler.category_router, prefix='/categories')
# router.include_router(product_handler.product_router, prefix='/products')
router.include_router(pet_images_handler.pet_images_router, prefix='/pet_images')
