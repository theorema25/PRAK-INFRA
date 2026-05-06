from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.controllers.event_controller import EventController
from src.database.connection import get_session
from src.dto.event_dto import EventCreate, EventUpdate
from src.middleware.auth_middleware import get_current_account, require_role

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/")
def get_events(
    db: Session = Depends(get_session),
    current_user: dict = Depends(get_current_account),
):
    controller = EventController(db)
    return controller.get_all()

@router.get("/{id}")
def get_event(
    id: int,
    db: Session = Depends(get_session),
    current_user: dict = Depends(get_current_account),
):
    controller = EventController(db)
    return controller.get_by_id(id)

@router.post("/", dependencies=[Depends(require_role("admin", "superadmin"))])
def create_event(event: EventCreate, db: Session = Depends(get_session)):
    controller = EventController(db)
    return controller.create(event)

@router.put("/{id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def update_event(id: int, event: EventUpdate, db: Session = Depends(get_session)):
    controller = EventController(db)
    return controller.update(id, event)

@router.delete("/{id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def delete_event(id: int, db: Session = Depends(get_session)):
    controller = EventController(db)
    return controller.delete(id)