from fastapi import APIRouter, Depends
from src.controllers import role_controller 
from src.middleware.auth_middleware import get_current_account, require_role

router = APIRouter(prefix="/roles", tags=["Roles"])

router.get("/", dependencies=[Depends(require_role("admin", "superadmin"))])(role_controller.get_roles)
router.get("/{role_id}", dependencies=[Depends(require_role("admin", "superadmin"))])(role_controller.get_role)
router.post("/", dependencies=[Depends(require_role("admin", "superadmin"))])(role_controller.create_role)
router.put("/{role_id}", dependencies=[Depends(require_role("admin", "superadmin"))])(role_controller.update_role)
router.delete("/{role_id}", dependencies=[Depends(require_role("admin", "superadmin"))])(role_controller.delete_role)