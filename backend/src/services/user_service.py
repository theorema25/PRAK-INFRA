from sqlmodel import Session
from src.repositories.user_repository import UserRepository
from src.database.model.models import User
from datetime import datetime
from fastapi import HTTPException


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def get_all_users(self, session: Session):
        return self.repository.get_all(session)

    def get_user(self, session: Session, user_id: int):
        user = self.repository.get_by_id(session, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create_user(self, session: Session, user_data):
        user = User(
            **user_data.dict(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.repository.create(session, user)

    def update_user(self, session: Session, user_id: int, user_data):
        user = self.repository.get_by_id(session, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(user, key, value)

        user.updated_at = datetime.now()

        return self.repository.update(session, user)

    def delete_user(self, session: Session, user_id: int):
        user = self.repository.get_by_id(session, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        self.repository.delete(session, user)
        return {"message": "User deleted successfully"}