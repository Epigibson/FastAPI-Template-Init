from uuid import UUID
from models.medical_history_model import MedicalHistory
from models.pet_model import Pet
from models.user_model import Usuario
from fastapi import HTTPException, status


class MedicalHistoryService:

    @staticmethod
    async def get_all_medical_histories():
        medical_histories = await MedicalHistory.find_all().to_list()
        if not medical_histories:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Medical histories not found."
            )
        return medical_histories

    @staticmethod
    async def create_medical_history_for_pet(pet_id: UUID, owner: Usuario):
        # Before create the medical history we need to check if the person who want to create it is veterinarian.
        if owner.user_type is not "Veterinarian":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"You are not a veterinarian, only Veterinarians can create a Medical History for a Pet."
            )

        # First we need to check if the pet exists, to confirm we need to get the pet.
        pet = await Pet.find_one(Pet.pet_id == pet_id)
        if not pet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pet not found."
            )
        # We need to store de owner of the pet in the medical history
        owner = await Usuario.find_one(Usuario.id == pet.owner)
        if not owner:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Owner not found."
            )
        if owner.address is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Owner address is empty, please fill your information."
            )
        if owner.mobile is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Owner mobile number is empty, please fill your information."
            )
        if owner.name is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Owner name is empty, please fill your information."
            )

        # Now we need to check if the medical history already exists for the pet.
        medical_history_check = await MedicalHistory.find_one(MedicalHistory.pet == pet.id)
        if medical_history_check:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Medical history already exists for this pet."
            )

        # Now we can create the medical history
        medical_history = MedicalHistory(
            pet=pet.id,
            owner=owner.id,
            pet_name=pet.name,
            pet_color=pet.color,
            pet_born_day=pet.born_day,
            pet_specie=pet.specie,
            pet_breed="None",
            pet_color_cast=pet.color_cast,
            pet_medical_conditions=pet.medical_conditions,
            owner_name=owner.name,
            owner_address=owner.address,
            owner_mobile_number=owner.mobile,
            owners_relationship="Owner",
        )

        await medical_history.insert()

        # We need to update the pet with the medical history id
        pet.medical_history = medical_history
        await pet.save()

        return medical_history

    @staticmethod
    async def get_medical_history_by_pet(pet_id: UUID) -> MedicalHistory:
        pet = await Pet.find_one(Pet.pet_id == pet_id)
        medical_history = await MedicalHistory.find_one(MedicalHistory.pet == pet.id)
        if not medical_history:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Medical history not found."
            )
        return medical_history
