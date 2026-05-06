from sqlmodel import Session, select
from src.database.model.models import Event # Penting: Path sesuai struktur Person 1

class EventRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.exec(select(Event)).all()

    def get_by_id(self, event_id: int):
        return self.db.get(Event, event_id)

    def create(self, event_data: dict):
        new_event = Event(**event_data)
        self.db.add(new_event)
        self.db.commit()
        self.db.refresh(new_event)
        return new_event

    def update(self, event_id: int, event_data: dict):
        db_event = self.get_by_id(event_id)
        if db_event:
            for key, value in event_data.items():
                if value is not None:
                    setattr(db_event, key, value)
            self.db.commit()
            self.db.refresh(db_event)
        return db_event

    def delete(self, event_id: int):
        db_event = self.get_by_id(event_id)
        if db_event:
            self.db.delete(db_event)
            self.db.commit()
            return True
        return False