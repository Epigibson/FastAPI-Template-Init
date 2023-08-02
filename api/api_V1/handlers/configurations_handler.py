from uuid import UUID
import pymongo.errors
from fastapi import APIRouter, HTTPException, status
from schemas.configuraciones_schema import ConfiguracionesCreate, ConfiguracionUpdate
from services.configuracion_services import ConfiguracionServices

configuraciones_router = APIRouter()


@configuraciones_router.post("/create", summary="Create a new configuration", tags=["Configuration"])
async def create(data: ConfiguracionesCreate):
    try:
        result = await ConfiguracionServices.create_configuracion(data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Can't create the configuration"
        )


@configuraciones_router.get("/", summary="List of configurations", tags=["Configuration"])
async def get_list():
    try:
        result = await ConfiguracionServices.get_configuracion()
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Can't get the configuration"
        )


@configuraciones_router.get("/{configuration_id}",  summary="Get configuration by id",
                            tags=["Configuration"])
async def retrieve(configuration_id: UUID):
    try:
        result = await ConfiguracionServices.get_configuracion_by_id(configuration_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Can't get the configuration"
        )


@configuraciones_router.put("/{configuration_id}",  summary="Update configuration", tags=["Configuration"])
async def update(configuration_id: UUID, data: ConfiguracionUpdate):
    try:
        result = await ConfiguracionServices.update_configuracion(configuration_id, data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Can't update the configuration"
        )


@configuraciones_router.delete("/{configuration_id}",   summary="Delete configuration",
                               tags=["Configuration"])
async def delete(configuration_id: UUID):
    try:
        result = await ConfiguracionServices.delete_configuracion(configuration_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Can't delete the configuration"
        )
