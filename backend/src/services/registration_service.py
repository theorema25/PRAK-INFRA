from fastapi import HTTPException
from src.repositories.registration_repository import RegistrationRepository
from src.dto.registration_dto import RegistrationCreate, RegistrationUpdate

class RegistrationService:
    def __init__(self, repository: RegistrationRepository):
        self.repository = repository

    def get_all_registrations(self):
        return self.repository.get_all()

    def get_registration_by_id(self, reg_id: int):
        reg = self.repository.get_by_id(reg_id)
        if not reg:
            raise HTTPException(status_code=404, detail="Registration not found")
        return reg

    def create_registration(self, reg_dto: RegistrationCreate):
        return self.repository.create(reg_dto.model_dump())

    def update_registration(self, reg_id: int, reg_dto: RegistrationUpdate):
        reg = self.repository.update(reg_id, reg_dto.model_dump(exclude_unset=True))
        if not reg:
            raise HTTPException(status_code=404, detail="Registration not found")
        return reg

    def delete_registration(self, reg_id: int):
        success = self.repository.delete(reg_id)
        if not success:
            raise HTTPException(status_code=404, detail="Registration not found")
        return {"message": "Registration deleted successfully"}