from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from api.api_V1.router import router
from core.config import settings
from core.description import DESCRIPTION
from core.update_fields import update_fields
from docs import tags_metadata
from models.notificaciones_model import Notificaciones
from models.pet_images import PetImage
from models.user_model import Usuario
from models.veterianrian_info_model import VeterinarianInfo
from models.role_model import Role
from models.permission_model import Permission
from models.pet_model import Pet
from models.category_model import Category
from models.product_model import Product
from models.medical_history_model import (MedicalHistory, VaccinesHistory, DewormingHistory, AllergyHistory,
                                          FoodAndDietInformation, MedicalProcedures, MedicalConsultations,
                                          LaboratoryAnalysis, FollowUpNotes, Medicines)

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

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).MICHICONDRIA

    await init_beanie(
        database=db_client,
        document_models=[
            Notificaciones,
            Usuario,
            VeterinarianInfo,
            Role,
            Pet,
            PetImage,
            Category,
            Product,
            MedicalHistory,
            VaccinesHistory, DewormingHistory, AllergyHistory,
            FoodAndDietInformation, MedicalProcedures, MedicalConsultations,
            LaboratoryAnalysis, FollowUpNotes, Medicines,
            Permission,
        ]
    )

    # Llama a la función para actualizar privado
    await update_fields()

app.include_router(router, prefix=settings.API_V1_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
