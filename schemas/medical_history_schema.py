from datetime import datetime
from typing import List, Optional
from uuid import UUID
from beanie import PydanticObjectId, Link
from pydantic import BaseModel, Field
from models.medical_history_model import VaccinesHistory, DewormingHistory, AllergyHistory, MedicalConsultations, \
    MedicalProcedures, LaboratoryAnalysis, FoodAndDietInformation


class MedicalHistoryOut(BaseModel):
    medical_history_id: UUID

    pet: PydanticObjectId
    owner: PydanticObjectId

    pet_name: str
    pet_color: str
    pet_born_day: str
    pet_specie: str
    pet_color_cast: str
    pet_medical_conditions: str

    owner_name: str
    owner_address: str
    owner_mobile_number: str
    owners_relationship: str

    vaccine_history: List[Link[VaccinesHistory]]
    deworming_history: List[Link[DewormingHistory]]
    allergy_history: List[Link[AllergyHistory]]
    dates_of_previous_visits: List[str]
    medical_consultations: List[Link[MedicalConsultations]]

    medical_procedures: List[Link[MedicalProcedures]]
    laboratory_analysis: List[Link[LaboratoryAnalysis]]
    food_and_diet_information: List[Link[FoodAndDietInformation]]
    consents_and_authorizations: bytes

    created_at: datetime
    updated_at: datetime


class MedicalHistoryUpdate(BaseModel):
    owner_address: Optional[str] = Field()
    owners_relationship: Optional[str] = Field()
