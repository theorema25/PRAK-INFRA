from sqlmodel import Session, select
from src.database.model.models import Account

class AuthRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_email_or_username(self, identifier: str) -> Account | None:
        statement = select(Account).where(
            (Account.email == identifier) | (Account.username == identifier)
        )
        return self.session.exec(statement).first()