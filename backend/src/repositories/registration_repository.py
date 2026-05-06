from sqlmodel import Session, select
from src.database.model.models import Registration

class RegistrationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.exec(select(Registration)).all()

    def get_by_id(self, reg_id: int):
        return self.db.get(Registration, reg_id)

    def create(self, reg_data: dict):
        new_reg = Registration(**reg_data)
        self.db.add(new_reg)
        self.db.commit()
        self.db.refresh(new_reg)
        return new_reg

    def update(self, reg_id: int, reg_data: dict):
        db_reg = self.get_by_id(reg_id)
        if db_reg:
            for key, value in reg_data.items():
                if value is not None:
                    setattr(db_reg, key, value)
            self.db.commit()
            self.db.refresh(db_reg)
        return db_reg

    def delete(self, reg_id: int):
        db_reg = self.get_by_id(reg_id)
        if db_reg:
            self.db.delete(db_reg)
            self.db.commit()
            return True
        return False