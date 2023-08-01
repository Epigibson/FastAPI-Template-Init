from uuid import UUID
import pymongo.errors
from fastapi import APIRouter, HTTPException, status
from schemas.configuraciones_schema import ConfiguracionesCreate, ConfiguracionUpdate
from services.configuracion_services import ConfiguracionServices

configuraciones_router = APIRouter()


@configuraciones_router.post("/create", summary="Crear configuracion", tags=["Configuraciones"])
async def create_configuracion(data: ConfiguracionesCreate):
    try:
        result = await ConfiguracionServices.create_configuracion(data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se pudo crear la configuracion"
        )


@configuraciones_router.get("/list", summary="Listar configuraciones", tags=["Configuraciones"])
async def get_configuraciones():
    try:
        result = await ConfiguracionServices.get_configuracion()
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron ventas"
        )


@configuraciones_router.get("/get_by_id/{configuracion_id}",  summary="Obtener configuracion por id",
                            tags=["Configuraciones"])
async def get_configuracion_by_id(configuracion_id: UUID):
    try:
        result = await ConfiguracionServices.get_configuracion_by_id(configuracion_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron ventas"
        )


@configuraciones_router.put("/update/{configuracion_id}",  summary="Actualizar configuracion", tags=["Configuraciones"])
async def update_configuracion(configuracion_id: UUID, data: ConfiguracionUpdate):
    try:
        result = await ConfiguracionServices.update_configuracion(configuracion_id, data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se pudo actualizar la configuracion"
        )


@configuraciones_router.delete("/delete/{configuracion_id}",   summary="Eliminar configuracion",
                               tags=["Configuraciones"])
async def delete_configuracion(configuracion_id: UUID):
    try:
        result = await ConfiguracionServices.delete_configuracion(configuracion_id)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se pudo eliminar la configuracion"
        )
