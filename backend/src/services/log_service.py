from sqlmodel import Session, select
from src.database.model.models import Log
from src.dto.log_dto import LogCreate
from datetime import datetime

class LogService:
    def get_logs(self, db: Session):
        return db.exec(select(Log)).all()

    def get_log(self, db: Session, log_id: int):
        return db.get(Log, log_id)

    def create_log(self, db: Session, data: LogCreate):
        log = Log(
            account_id=data.account_id,
            action=data.action,
            ip_address=data.ip_address,
            user_agent=data.user_agent,
            entity=data.entity,
            entity_id=data.entity_id,
            created_at=datetime.now()
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def delete_log(self, db: Session, log_id: int):
        log = db.get(Log, log_id)
        if log:
            db.delete(log)
            db.commit()
            return True
        return False
