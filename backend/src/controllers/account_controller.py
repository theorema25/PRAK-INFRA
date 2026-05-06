from fastapi import Depends, HTTPException
from sqlmodel import Session
from src.services.account_service import AccountService
from src.database.connection import get_session
from src.dto.account_dto import AccountCreate, AccountUpdate


service = AccountService()


def get_accounts(db: Session = Depends(get_session)):
    try:
        return service.get_accounts(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_account(account_id: int, db: Session = Depends(get_session)):
    try:
        result = service.get_account(db, account_id)
        if not result:
            raise HTTPException(status_code=404, detail="Account tidak ditemukan")
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def create_account(data: AccountCreate, db: Session = Depends(get_session)):
    try:
        return service.create_account(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def update_account(account_id: int, data: AccountUpdate, db: Session = Depends(get_session)):
    try:
        result = service.update_account(db, account_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Account tidak ditemukan")
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def delete_account(account_id: int, db: Session = Depends(get_session)):
    try:
        result = service.delete_account(db, account_id)
        if not result:
            raise HTTPException(status_code=404, detail="Account tidak ditemukan")
        return {"message": "Account berhasil dihapus"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))