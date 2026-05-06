from fastapi import HTTPException
from src.repositories.event_repository import EventRepository
from src.dto.event_dto import EventCreate, EventUpdate

class EventService:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def get_all_events(self):
        return self.repository.get_all()

    def get_event_by_id(self, event_id: int):
        event = self.repository.get_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event

    def create_event(self, event_dto: EventCreate):
        # Menggunakan model_dump() untuk Pydantic v2 (FastAPI standar baru)
        return self.repository.create(event_dto.model_dump())

    def update_event(self, event_id: int, event_dto: EventUpdate):
        event = self.repository.update(event_id, event_dto.model_dump(exclude_unset=True))
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event

    def delete_event(self, event_id: int):
        success = self.repository.delete(event_id)
        if not success:
            raise HTTPException(status_code=404, detail="Event not found")
        return {"message": "Event deleted successfully"}