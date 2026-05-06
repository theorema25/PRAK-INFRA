from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.repositories.auth_repository import AuthRepository
from src.dto.auth_dto import LoginRequest, TokenResponse, RegisterRequest
from src.utils.security import verify_password, create_access_token, hash_password
from src.database.model.models import User, Account, Role
from datetime import datetime


class AuthService:
    def __init__(self, session: Session):
        self.session = session
        self.repo = AuthRepository(session)

    def login(self, payload: LoginRequest) -> TokenResponse:
        account = self.repo.find_by_email_or_username(payload.identifier)

        if not account:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email/username atau password salah"
            )

        password_valid = verify_password(payload.password, account.password)

        if not password_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email/username atau password salah"
            )

        token_data = {
            "sub": str(account.id),
            "user_id": account.user_id,
            "role": account.role.name if account.role else None,
        }

        token = create_access_token(token_data)

        return TokenResponse(
            access_token=token,
            account_id=account.id,
            user_id=account.user_id,
            role=account.role.name if account.role else ""
        )

    def register(self, payload: RegisterRequest):
        if not payload.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password tidak boleh kosong"
            )

        existing_account = self.repo.find_by_email_or_username(payload.email)
        if not existing_account:
            existing_account = self.repo.find_by_email_or_username(payload.username)

        if existing_account:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email atau username sudah terdaftar"
            )

        hashed_password = hash_password(payload.password)

        user = User(
            first_name=payload.username,
            last_name="",
            whatsapp="",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        role = self.session.exec(select(Role).where(Role.name == "user")).first()
        if not role:
            role = Role(name="user")
            self.session.add(role)
            self.session.commit()
            self.session.refresh(role)

        account = Account(
            username=payload.username,
            email=payload.email,
            password=hashed_password,
            user_id=user.id,
            role_id=role.id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)

        return {
            "username": account.username,
            "email": account.email
        }