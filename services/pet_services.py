import re
from typing import Optional
from uuid import UUID
from models.pet_model import Pet
from models.user_model import Usuario
from schemas.pet_schema import PetCreate, PetUpdate

from fastapi import HTTPException, status, Query


class PetService:

    @staticmethod
    async def get_all_pets(owner: Usuario,
                           name: Optional[str] = Query(None),
                           nickname: Optional[str] = Query(None),
                           specie: Optional[str] = Query(None)) -> list[Pet]:
        filter_query = {
            key:  value.lower() if value is not None else None
            for key, value in {
                "name": name,
                "nickname":  nickname,
                "specie": specie
            }.items()
        }

        filter_conditions = [Pet.owner == owner.id]

        for key, value in filter_query.items():
            if value is not None:
                regex_pattern = f".*{re.escape(value)}.*"  # Convert the value to a regex pattern
                filter_conditions.append({key: {"$regex": regex_pattern, "$options": "i"}})

        result = await Pet.find({"$and": filter_conditions}).to_list()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pets not found"
            )
        return result

    @staticmethod
    async def get_pet_by_id(pet_id: UUID, owner: Usuario):
        result = await Pet.find_one(Pet.owner == owner.id, Pet.pet_id == pet_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pet not found"
            )
        return result

    @staticmethod
    async def create_pet(owner: Usuario, data: PetCreate):
        result = Pet(**data.dict(), owner=owner.id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Can't create pet"
            )
        await result.insert()
        return result

    @staticmethod
    async def update_pet(pet_id: UUID, owner: Usuario, data: PetUpdate):
        result = await PetService.get_pet_by_id(pet_id, owner)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pet not found"
            )
        await result.update({"$set": data.dict(exclude_unset=True)})
        return result

    @staticmethod
    async def delete_pet(pet_id: UUID, owner: Usuario):
        result = await Pet.find_one(Pet.owner == owner.id, Pet.pet_id == pet_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pet not found"
            )
        await result.delete()
        return result
