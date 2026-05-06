from sqlmodel import Session, select
from src.database.model.models import Role


class RoleRepository:

    def get_all(self, db: Session):
        return db.exec(select(Role)).all()

    def get_by_id(self, db: Session, role_id: int):
        return db.get(Role, role_id)

    def create(self, db: Session, role: Role):
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def update(self, db: Session, role: Role):
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def delete(self, db: Session, role_id: int):
        role = db.get(Role, role_id)
        if role:
            db.delete(role)
            db.commit()
            return True
        return False