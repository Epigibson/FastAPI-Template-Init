from uuid import UUID
import pymongo.errors
from fastapi import APIRouter, HTTPException, status, Depends

from api.deps.user_deps import get_current_user
from models.user_model import Usuario
from services.medical_history_services import MedicalHistoryService

medical_history_router = APIRouter()


@medical_history_router.get("/", summary="Get medical history", tags=["Medical History"])
async def get_medical_history():
    try:
        result = await MedicalHistoryService.get_all_medical_histories()
        return result
    except pymongo.errors.OperationFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )


@medical_history_router.post("/{pet_id}", summary="Create medical history", tags=["Medical History"])
async def create_medical_history(pet_id: UUID, owner: Usuario = Depends(get_current_user)):
    try:
        result = await MedicalHistoryService.create_medical_history_for_pet(pet_id, owner)
        return result
    except pymongo.errors.OperationFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )


@medical_history_router.get("/{pet_id}", summary="Get medical history by pet", tags=["Medical History"])
async def get_medical_history_by_pet(pet_id: UUID):
    try:
        result = await MedicalHistoryService.get_medical_history_by_pet(pet_id)
        return result
    except pymongo.errors.OperationFailure as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
