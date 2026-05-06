from sqlmodel import Session, select
from src.database.model.models import User


class UserRepository:

    def get_all(self, session: Session):
        statement = select(User)
        return session.exec(statement).all()

    def get_by_id(self, session: Session, user_id: int):
        return session.get(User, user_id)

    def create(self, session: Session, user: User):
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except Exception as e:
            print("❌ ERROR DB:", str(e))
            session.rollback()
            raise

    def update(self, session: Session, user: User):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def delete(self, session: Session, user: User):
        session.delete(user)
        session.commit()