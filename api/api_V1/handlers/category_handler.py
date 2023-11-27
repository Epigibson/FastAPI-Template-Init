from typing import Optional
import pymongo.errors
from fastapi import APIRouter, Query, HTTPException, status
from schemas.category_schema import CategoryCreate, CategoryUpdate
from services.category_services import CategoryService
from uuid import UUID

category_router = APIRouter()


@category_router.get("/", summary="Get all categories", tags=["Category"])
async def get_all_categories(category_name: Optional[str] = Query(None)):
    try:
        result = await CategoryService.get_all_categories(category_name)
        return result
    except pymongo.errors.PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Can't retrieve categories. {e}"
        )


@category_router.get("/{category_id}", summary="Get category by ID", tags=["Category"])
async def get_category_by_id(category_id: UUID):
    try:
        result = await CategoryService.get_category(category_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't retrieve category."
        )


@category_router.post("/", summary="Create category", tags=["Category"])
async def create_category(data: CategoryCreate):
    try:
        result = await CategoryService.create_category(data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't create category."
        )


@category_router.put("/{category_id}", summary="Update category", tags=["Category"])
async def update_category(category_id: UUID, data: CategoryUpdate):
    try:
        result = await CategoryService.update_category(category_id, data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't update category."
        )


@category_router.delete("/{category_id}", summary="Delete category", tags=["Category"])
async def delete_category(category_id: UUID):
    try:
        result = await CategoryService.delete_category(category_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't delete category."
        )