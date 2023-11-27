from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4
from beanie import Document, PydanticObjectId, Link, Indexed
from pydantic import Field


class VaccinesHistory(Document):
    who_applied: PydanticObjectId
    vaccines_history_id: UUID = Field(default_factory=uuid4, unique=True)
    vaccine_name: Indexed(str, unique=True)
    vaccine_brand: str = Field()
    vaccine_batch: str = Field()
    application_date: str = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Vaccines History"


class DewormingHistory(Document):
    who_applied: PydanticObjectId
    deworming_history_id: UUID = Field(default_factory=uuid4, unique=True)
    deworming_name: Indexed(str, unique=True)
    deworming_brand: str = Field()
    application_date: str = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Deworming History"


class AllergyHistory(Document):
    allergy_history_id: Indexed(UUID) = Field(default_factory=uuid4, unique=True)
    allergy_name: str = Field(unique=True)
    allergy_type: str = Field()
    date_of_appearance: str = Field()
    date_of_disappearance: str = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Allergy History"


class Medicines(Document):
    medicine_id: UUID = Field(default_factory=uuid4, unique=True)
    medicine_name: Indexed(str, unique=True)
    medicine_brand: str = Field()
    medicine_laboratory: str = Field()
    medicine_presentation: str = Field()

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Medicines"


class MedicalConsultations(Document):
    medical_consultations_id: Indexed(UUID) = Field(default_factory=uuid4, unique=True)
    date: datetime = Field(default_factory=datetime.utcnow)

    veterinarian: PydanticObjectId
    veterinarian_name: str = Field()
    veterinary_id: str = Field()

    pets_owner: str = Field()
    pet_name: str = Field()
    pet_weight: float = Field()
    pet_age: int = Field()
    reason: str = Field()
    diagnosis: str = Field()

    medicines: List[Link[Medicines]]
    dosage_and_indications: str = Field()

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Medical Consultations"


class MedicalProcedures(Document):
    who_performed: PydanticObjectId
    medical_procedure_id: Indexed(UUID) = Field(default_factory=uuid4, unique=True)
    name_of_procedure: str = Field()
    type_of_procedure: str = Field()
    date_of_procedure: str = Field()
    description_of_procedure: str = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Medical Procedures"


class LaboratoryAnalysis(Document):
    who_prescribed: PydanticObjectId
    laboratory_analysis_id: Indexed(UUID) = Field(default_factory=uuid4, unique=True)
    laboratory_analysis_name: str = Field()
    laboratory_analysis_type: str = Field()
    laboratory_analysis_date: str = Field()
    laboratory_analysis_file: bytes = Field(default_factory=bytes)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Laboratory Analysis"


class FoodAndDietInformation(Document):
    who_prescribed: PydanticObjectId
    food_and_diet_information_id: Indexed(UUID) = Field(default_factory=uuid4, unique=True)
    food_type: str = Field()
    food_brand: str = Field()
    feeding_frequency: str = Field()
    intolerances: str = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Food And Diet Information"


class FollowUpNotes(Document):
    follow_up_notes_id: Indexed(UUID) = Field(default_factory=uuid4, unique=True)
    follow_up_details: str = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    class Config:
        orm_mode = True

    class Settings:
        name = "Follow-Up Notes"


class MedicalHistory(Document):
    medical_history_id: Indexed(UUID) = Field(default_factory=uuid4, unique=True)

    pet: PydanticObjectId = Field()
    owner: PydanticObjectId = Field()

    pet_name: str = Field()
    pet_color: str = Field()
    pet_born_day: str = Field(max_length=80)
    pet_specie: str = Field()
    pet_color_cast: str = Field()
    pet_medical_conditions: str = Field()

    owner_name: str = Field()
    owner_address: str = Field()
    owner_mobile_number: str = Field()
    owners_relationship: str = Field()

    vaccine_history: Optional[List[Link[VaccinesHistory]]] = Field([])
    deworming_history: Optional[List[Link[DewormingHistory]]] = Field([])
    allergy_history: Optional[List[Link[AllergyHistory]]] = Field([])
    dates_of_previous_visits: Optional[List[str]] = Field([])
    medical_consultations: Optional[List[Link[MedicalConsultations]]] = Field([])

    medical_procedures: Optional[List[Link[MedicalProcedures]]] = Field([])
    laboratory_analysis: Optional[List[Link[LaboratoryAnalysis]]] = Field([])
    food_and_diet_information: Optional[List[Link[FoodAndDietInformation]]] = Field([])
    consents_and_authorizations: Optional[bytes] = Field(default_factory=bytes)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def commit(self):
        self.save()

    def __unicode__(self):
        return self.medical_history_id

    class Config:
        orm_mode = True

    class Settings:
        name = "Medical History"
