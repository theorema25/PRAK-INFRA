from fastapi import Depends
from sqlmodel import Session
from src.services.role_service import RoleService
from src.database.connection import get_session
from src.dto.role_dto import RoleCreate, RoleUpdate

service = RoleService()

def get_roles(db: Session = Depends(get_session)):
    """Mengambil semua data role dari database"""
    return service.get_roles(db)

def get_role(role_id: int, db: Session = Depends(get_session)):
    """Mengambil satu data role spesifik berdasarkan ID"""
    return service.get_role(db, role_id)

def create_role(data: RoleCreate, db: Session = Depends(get_session)):
    """Membuat role baru dengan validasi RoleCreate DTO"""
    return service.create_role(db, data)

def update_role(role_id: int, data: RoleUpdate, db: Session = Depends(get_session)):
    """Mengupdate data role yang ada menggunakan RoleUpdate DTO"""
    return service.update_role(db, role_id, data)

def delete_role(role_id: int, db: Session = Depends(get_session)):
    """Menghapus role dari sistem"""
    return service.delete_role(db, role_id)