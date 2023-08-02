from uuid import UUID
import pymongo.errors
from fastapi import HTTPException, status, APIRouter
from schemas.permission_schema import PermissionCreate, PermissionUpdate
from services.permission_services import PermissionServices

permission_router = APIRouter()


@permission_router.post("/create", summary="Create a new permission", tags=["Permission"])
async def create(data: PermissionCreate):
    try:
        result = await PermissionServices.create(data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't create the new permission"
        )


@permission_router.get("/", summary="List all permissions", tags=["Permission"])
async def get_list():
    try:
        result = await PermissionServices.list()
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't list all permissions"
        )


@permission_router.get("/{role_id}", summary="Get a permission by id", tags=["Permission"])
async def retrieve(role_id: UUID):
    try:
        result = await PermissionServices.retrieve(role_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't get the permission"
        )


@permission_router.put("/{role_id}", summary="Update a permission by id", tags=["Permission"])
async def update(role_id: UUID, data: PermissionUpdate):
    try:
        result = await PermissionServices.update(role_id, data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't update the permission"
        )


@permission_router.delete("/{role_id}", summary="Delete a permission by id", tags=["Permission"])
async def delete(role_id: UUID):
    try:
        result = await PermissionServices.delete(role_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't delete the permission"
        )
