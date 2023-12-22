import re
from pathlib import Path
from typing import Optional, List
from uuid import UUID
from models.pet_model import Pet
from models.user_model import Usuario
from schemas.pet_schema import PetCreate, PetUpdate

from fastapi import HTTPException, status, Query, UploadFile


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
    async def create_pet(data: PetCreate, owner: Usuario):
        pet = Pet(**data.dict(), owner=owner.id)
        await pet.insert()
        return pet

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
    async def update_pet_images(pet_id: UUID, owner: Usuario, new_images: List[UploadFile]):
        pet = await PetService.get_pet_by_id(pet_id, owner)

        if new_images:
            images_directory = Path("path/to/your/image/directory")
            images_directory.mkdir(parents=True, exist_ok=True)  # Crea el directorio si no existe

            for image in new_images:
                file_location = images_directory / image.filename
                with open(file_location, "wb+") as file_object:
                    file_object.write(await image.read())
                pet.profile_images.append(str(file_location))

        await pet.save()
        return pet

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
