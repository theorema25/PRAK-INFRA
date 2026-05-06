from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import api_router
from src.database.connection import create_db_and_tables

app = FastAPI(
    title="Event API",
    description="API untuk manajemen event",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "API is running"}