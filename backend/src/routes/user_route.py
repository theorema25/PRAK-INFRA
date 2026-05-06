from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.controllers.user_controller import UserController
from src.dto.user_dto import UserCreate, UserUpdate
from src.database.connection import get_session
from src.middleware.auth_middleware import get_current_account, require_role

router = APIRouter(prefix="/users", tags=["Users"])
controller = UserController()

@router.get("/", dependencies=[Depends(require_role("admin", "superadmin"))])
def get_users(session: Session = Depends(get_session)):
    return controller.get_all(session)

@router.get("/{user_id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def get_user(user_id: int, session: Session = Depends(get_session)):
    return controller.get_by_id(user_id, session)

@router.post("/", dependencies=[Depends(require_role("admin", "superadmin"))])
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    try:
        return controller.create(user, session)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

@router.put("/{user_id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def update_user(user_id: int, user: UserUpdate, session: Session = Depends(get_session)):
    return controller.update(user_id, user, session)

@router.delete("/{user_id}", dependencies=[Depends(require_role("admin", "superadmin"))])
def delete_user(user_id: int, session: Session = Depends(get_session)):
    return controller.delete(user_id, session)