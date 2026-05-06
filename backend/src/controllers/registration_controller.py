from sqlmodel import Session
from src.services.registration_service import RegistrationService
from src.repositories.registration_repository import RegistrationRepository
from src.dto.registration_dto import RegistrationCreate, RegistrationUpdate

class RegistrationController:
    def __init__(self, db: Session):
        repo = RegistrationRepository(db)
        self.service = RegistrationService(repo)

    def get_all(self):
        return self.service.get_all_registrations()

    def get_by_id(self, reg_id: int):
        return self.service.get_registration_by_id(reg_id)

    def create(self, reg: RegistrationCreate):
        return self.service.create_registration(reg)

    def update(self, reg_id: int, reg: RegistrationUpdate):
        return self.service.update_registration(reg_id, reg)

    def delete(self, reg_id: int):
        return self.service.delete_registration(reg_id)