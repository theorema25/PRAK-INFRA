from fastapi import APIRouter
from src.routes.account_route import router as account_router
from src.routes.event_route import router as event_router
from src.routes.registration_route import router as registration_router
from src.routes.role_route import router as role_router
from src.routes.user_route import router as user_router
from src.routes.auth_route import router as auth_router

api_router = APIRouter()

api_router.include_router(account_router)
api_router.include_router(event_router)
api_router.include_router(user_router)
api_router.include_router(role_router)
api_router.include_router(registration_router)
api_router.include_router(auth_router)