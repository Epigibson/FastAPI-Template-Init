from uuid import UUID
import pymongo.errors
from fastapi import APIRouter, HTTPException, status
from services.pet_images_services import PetImageService

pet_images_router = APIRouter()


@pet_images_router.get("/", summary="Get all pet images", tags=["Pet Images"])
async def get_all_pet_images():
    try:
        result = await PetImageService.get_all_images()
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't retrieve pets."
        )


@pet_images_router.get("/pet/{pet_id}", summary="Get all pet images by pet ID", tags=["Pet Images"])
async def get_all_pet_images_by_pet_id(pet_id: UUID):
    try:
        result = await PetImageService.get_images_from_pet(pet_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't retrieve pets."
        )
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet images not found."
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error."
        )


@pet_images_router.get("/{image_id}", summary="Get pet image by ID", tags=["Pet Images"])
async def get_pet_image_by_id(image_id: UUID):
    try:
        result = await PetImageService.get_image_by_id(image_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't retrieve pet."
        )
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet image not found."
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error."
        )


@pet_images_router.delete("/{image_id}", summary="Delete pet image by ID", tags=["Pet Images"])
async def delete_pet_image_by_id(image_id: UUID):
    try:
        result = await PetImageService.delete_image_by_id(image_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't delete pet."
        )
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet image not found."
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error."
        )
