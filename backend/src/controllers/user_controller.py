from sqlmodel import Session
from src.services.user_service import UserService


class UserController:

    def __init__(self):
        self.service = UserService()

    def get_all(self, session: Session):
        return self.service.get_all_users(session)

    def get_by_id(self, user_id: int, session: Session):
        return self.service.get_user(session, user_id)

    def create(self, user_data, session: Session):
        return self.service.create_user(session, user_data)

    def update(self, user_id: int, user_data, session: Session):
        return self.service.update_user(session, user_id, user_data)

    def delete(self, user_id: int, session: Session):
        return self.service.delete_user(session, user_id)
