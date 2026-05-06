from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional


class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    accounts: list["Account"] = Relationship(back_populates="role")


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: Optional[str] = Field(default=None, max_length=255)
    last_name: Optional[str] = Field(default=None, max_length=255)
    whatsapp: Optional[str] = Field(default=None, max_length=30)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    accounts: list["Account"] = Relationship(back_populates="user")
    registrations: list["Registration"] = Relationship(back_populates="user")


class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    role_id: Optional[int] = Field(default=None, foreign_key="roles.id")

    email: Optional[str] = None
    username: Optional[str] = Field(default=None, max_length=16)
    password: Optional[str] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    user: Optional[User] = Relationship(back_populates="accounts")
    role: Optional[Role] = Relationship(back_populates="accounts")

    logs: list["Log"] = Relationship(back_populates="account")


class Event(SQLModel, table=True):
    __tablename__ = "events"

    id: Optional[int] = Field(default=None, primary_key=True)

    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None

    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    registrations: list["Registration"] = Relationship(back_populates="event")


class Registration(SQLModel, table=True):
    __tablename__ = "registrations"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    event_id: Optional[int] = Field(default=None, foreign_key="events.id")

    user: Optional[User] = Relationship(back_populates="registrations")
    event: Optional[Event] = Relationship(back_populates="registrations")


class Log(SQLModel, table=True):
    __tablename__ = "logs"

    id: Optional[int] = Field(default=None, primary_key=True)

    account_id: Optional[int] = Field(default=None, foreign_key="accounts.id")

    created_at: Optional[datetime] = None
    action: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None

    entity: Optional[str] = None
    entity_id: Optional[int] = None

    account: Optional[Account] = Relationship(back_populates="logs")