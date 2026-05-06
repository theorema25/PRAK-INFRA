from fastapi import Depends
from sqlmodel import Session
from src.services.log_service import LogService
from src.database.connection import get_session
from src.dto.log_dto import LogCreate

service = LogService()

def get_logs(db: Session = Depends(get_session)):
    return service.get_logs(db)

def get_log(log_id: int, db: Session = Depends(get_session)):
    return service.get_log(db, log_id)

def create_log(data: LogCreate, db: Session = Depends(get_session)):
    return service.create_log(db, data)

def delete_log(log_id: int, db: Session = Depends(get_session)):
    return service.delete_log(db, log_id)