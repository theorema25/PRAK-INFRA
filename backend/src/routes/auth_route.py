from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.database.connection import get_session
from src.services.auth_service import AuthService
from src.dto.auth_dto import LoginRequest, TokenResponse, RegisterRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, session: Session = Depends(get_session)):
    service = AuthService(session)
    return service.login(payload)


@router.post("/register")
def register(payload: RegisterRequest, session: Session = Depends(get_session)):
    try:
        service = AuthService(session)
        result = service.register(payload)

        return {
            "message": "Registrasi berhasil",
            "data": result
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))