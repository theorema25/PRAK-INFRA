from sqlmodel import Session, select
from src.database.model.models import Account


class AccountRepository:

    def get_all(self, db: Session):
        return db.exec(select(Account)).all()

    def get_by_id(self, db: Session, account_id: int):
        return db.get(Account, account_id)

    def create(self, db: Session, account: Account):
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def update(self, db: Session, account: Account):
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def delete(self, db: Session, account_id: int):
        account = db.get(Account, account_id)
        if account:
            db.delete(account)
            db.commit()
            return True
        return False
