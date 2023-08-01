from uuid import UUID
from models.configuraciones_model import Configuraciones
from schemas.configuraciones_schema import ConfiguracionesCreate, ConfiguracionUpdate
from typing import List


class ConfiguracionServices:

    @staticmethod
    async def create_configuracion(data: ConfiguracionesCreate) -> Configuraciones:
        result = Configuraciones(**data.dict())
        return await result.insert()

    @staticmethod
    async def get_configuracion() -> List[Configuraciones]:
        result = await Configuraciones.find_all().to_list()
        return result

    @staticmethod
    async def get_configuracion_by_id(configuracion_id: UUID) -> Configuraciones:
        result = await Configuraciones.find_one(Configuraciones.configuracion_id == configuracion_id)
        return result

    @staticmethod
    async def update_configuracion(configuracion_id: UUID, data: ConfiguracionUpdate) -> Configuraciones:
        result = await Configuraciones.find_one(Configuraciones.configuracion_id == configuracion_id)
        await result.update({"$set": data.dict(exclude_unset=True)})
        result.commit()
        return result

    @staticmethod
    async def delete_configuracion(configuracion_id: UUID) -> Configuraciones:
        result = await Configuraciones.find_one(Configuraciones.configuracion_id == configuracion_id)
        await result.delete()
        return result
