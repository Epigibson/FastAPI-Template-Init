from typing import Optional
from uuid import UUID

from fastapi import UploadFile

from models.pet_images import PetImage
import core.cloudinary_config
from cloudinary.uploader import upload

from models.pet_model import Pet
from services.pet_services import PetService


class PetImageService:

    @staticmethod
    async def get_all_images():
        result = await PetImage.find_all().to_list()
        return result

    @staticmethod
    async def get_images_from_pet(pet_id: UUID):
        result = await PetImage.find(PetImage.pet_id == pet_id).to_list()
        return result

    @staticmethod
    async def get_image_by_id(image_id: UUID):
        result = await PetImage.find_one(PetImage.pet_image_id == image_id)
        return result

    @staticmethod
    async def upload_image_for_pet(pet_id: UUID, images: Optional[list[UploadFile]] = None):
        pet = await Pet.find_one(Pet.pet_id == pet_id)
        images_url = []
        if images:
            for element in images:
                image = upload(element.file.read(), folder="pet_images", public_id=pet.name, overwrite=True, )
                images_url.append(image['url'])
        pet_image = PetImage(pet_id=pet_id, images=images_url)
        await pet_image.insert()

    @staticmethod
    async def delete_image_by_id(image_id: UUID):
        result = await PetImageService.get_image_by_id(image_id)
        if result:
            await result.delete()
            return True
        return False
