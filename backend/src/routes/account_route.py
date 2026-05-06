from fastapi import APIRouter, Depends
from src.controllers import account_controller
from src.middleware.auth_middleware import get_current_account, require_role

router = APIRouter(prefix="/accounts", tags=["Accounts"])

router.get("/", dependencies=[Depends(get_current_account)])(account_controller.get_accounts)
router.get("/{account_id}", dependencies=[Depends(get_current_account)])(account_controller.get_account)
router.post("/", dependencies=[Depends(require_role("admin", "superadmin"))])(account_controller.create_account)
router.put("/{account_id}", dependencies=[Depends(require_role("admin", "superadmin"))])(account_controller.update_account)
router.delete("/{account_id}", dependencies=[Depends(require_role("admin", "superadmin"))])(account_controller.delete_account)