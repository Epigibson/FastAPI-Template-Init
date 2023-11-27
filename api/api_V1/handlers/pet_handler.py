from typing import Optional
import pymongo.errors
from fastapi import APIRouter, HTTPException, status, Depends
from api.deps.user_deps import get_current_user
from models.pet_model import Pet
from models.user_model import Usuario
from schemas.pet_schema import PetUpdate, PetCreate
from services.pet_services import PetService
from uuid import UUID

pet_router = APIRouter()


@pet_router.get("/", summary="Get all pets", tags=["Pets"], response_model=list[Pet])
async def get_all_pets(owner: Usuario = Depends(get_current_user), name: Optional[str] = None,
                       nickname: Optional[str] = None, specie: Optional[str] = None):
    try:
        result = await PetService.get_all_pets(owner, name, nickname, specie)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't retrieve pets."
        )


@pet_router.get("/{pet_id}", summary="Get pet by ID", tags=["Pets"], response_model=Pet)
async def get_pet_by_id(pet_id: UUID, owner: Usuario = Depends(get_current_user)):
    try:
        result = await PetService.get_pet_by_id(pet_id, owner)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't retrieve pet."
        )


@pet_router.post("/", summary="Create pet", tags=["Pets"], response_model=Pet)
async def create_pet(data: PetCreate, owner: Usuario = Depends(get_current_user)):
    try:
        result = await PetService.create_pet(owner, data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't create pet."
        )


@pet_router.put("/{pet_id}", summary="Update pet by ID", tags=["Pets"], response_model=Pet)
async def update_pet_by_id(pet_id: UUID, data: PetUpdate, owner: Usuario = Depends(get_current_user)):
    try:
        result = await PetService.update_pet(pet_id, owner, data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't update pet."
        )


@pet_router.delete("/{pet_id}", summary="Delete pet by ID", tags=["Pets"])
async def delete_pet_by_id(pet_id: UUID, owner: Usuario = Depends(get_current_user)):
    try:
        result = await PetService.delete_pet(pet_id, owner)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't delete pet."
        )
