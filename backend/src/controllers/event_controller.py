from sqlmodel import Session
from src.services.event_service import EventService
from src.repositories.event_repository import EventRepository
from src.dto.event_dto import EventCreate, EventUpdate

class EventController:
    def __init__(self, db: Session):
        repo = EventRepository(db)
        self.service = EventService(repo)

    def get_all(self):
        return self.service.get_all_events()

    def get_by_id(self, event_id: int):
        return self.service.get_event_by_id(event_id)

    def create(self, event: EventCreate):
        return self.service.create_event(event)

    def update(self, event_id: int, event: EventUpdate):
        return self.service.update_event(event_id, event)

    def delete(self, event_id: int):
        return self.service.delete_event(event_id)