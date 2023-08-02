from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from api.api_V1.router import router
from core.config import settings
from core.description import DESCRIPTION
from docs import tags_metadata
from models.notificaciones_model import Notificaciones
from models.user_model import Usuario
from models.todo_model import Todo
from models.role_model import Role
from models.permission_model import Permission

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=DESCRIPTION,
    version="1.0.0(Alpha)",
    openapi_tags=tags_metadata,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    debug=False
)


@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).WMG

    await init_beanie(
        database=db_client,
        document_models=[
            Notificaciones,
            Usuario,
            Todo,
            Role,
            Permission,
        ]
    )
app.include_router(router, prefix=settings.API_V1_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
