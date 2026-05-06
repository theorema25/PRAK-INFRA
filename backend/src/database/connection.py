from sqlmodel import create_engine, SQLModel, Session
from src.database.model.models import *

DATABASE_URL = "postgresql://postgres:1234@localhost:5433/acara_rsi"

engine = create_engine(DATABASE_URL, echo=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session