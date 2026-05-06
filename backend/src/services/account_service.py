from sqlmodel import Session
from src.repositories.account_repository import AccountRepository
from src.database.model.models import Account
from src.utils.security import hash_password
from datetime import datetime


class AccountService:

    def __init__(self):
        self.repo = AccountRepository()

    def get_accounts(self, db: Session):
        return self.repo.get_all(db)

    def get_account(self, db: Session, account_id: int):
        return self.repo.get_by_id(db, account_id)

    def create_account(self, db: Session, data):
        account = Account(
            user_id=data.user_id,
            role_id=data.role_id,
            email=data.email,
            username=data.username,
            password=hash_password(data.password),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.repo.create(db, account)

    def update_account(self, db: Session, account_id: int, data):
        account = self.repo.get_by_id(db, account_id)
        if not account:
            return None

        if data.user_id is not None:
            account.user_id = data.user_id
        if data.role_id is not None:
            account.role_id = data.role_id
        if data.email is not None:
            account.email = data.email
        if data.username is not None:
            account.username = data.username
        if data.password is not None:
            account.password = hash_password(data.password)

        account.updated_at = datetime.now()

        return self.repo.update(db, account)

    def delete_account(self, db: Session, account_id: int):
        account = self.repo.get_by_id(db, account_id)
        if not account:
            return None

        self.repo.delete(db, account_id)
        return account