from sqlmodel import Session, select
from datetime import datetime, timedelta
from src.database.connection import engine
from src.database.model.models import (
    Role, User, Account, Event, Registration, Log
)
from src.utils.security import hash_password

def now():
    return datetime.utcnow()


def seed_roles(session: Session):
    if session.exec(select(Role)).first():
        print("Roles already seeded")
        return

    roles = [
        Role(name="user"),
        Role(name="admin"),
        Role(name="superadmin"),
    ]

    session.add_all(roles)
    session.commit()
    print("Seeded roles: user, admin, superadmin")


def seed_users(session: Session):
    if session.exec(select(User)).first():
        print("Users already seeded")
        return

    users = [
        User(
            first_name=f"User{i}",
            last_name="Test",
            whatsapp=f"08123{i:05}",
            created_at=now(),
            updated_at=now(),
        )
        for i in range(1, 11)
    ]

    session.add_all(users)
    session.commit()
    print("Seeded users")


def seed_accounts(session: Session):
    if session.exec(select(Account)).first():
        print("Accounts already seeded")
        return

    users = session.exec(select(User)).all()
    roles = {r.name: r for r in session.exec(select(Role)).all()}

    role_user       = roles.get("user")
    role_admin      = roles.get("admin")
    role_superadmin = roles.get("superadmin")

    accounts = []

    # 1 superadmin
    accounts.append(
        Account(
            user_id=users[0].id,
            role_id=role_superadmin.id,
            email="superadmin@mail.com",
            username="superadmin",
            password=hash_password("superadmin123"),
            created_at=now(),
            updated_at=now(),
        )
    )

    # 3 admin (user index 1-3)
    for i in range(1, 4):
        accounts.append(
            Account(
                user_id=users[i].id,
                role_id=role_admin.id,
                email=f"admin{i}@mail.com",
                username=f"admin{i}",
                password=hash_password("password123"),
                created_at=now(),
                updated_at=now(),
            )
        )

    # 6 user (user index 4-9)
    for i in range(4, 10):
        accounts.append(
            Account(
                user_id=users[i].id,
                role_id=role_user.id,
                email=f"user{i+1}@mail.com",
                username=f"user{i+1}",
                password=hash_password("password123"),
                created_at=now(),
                updated_at=now(),
            )
        )

    session.add_all(accounts)
    session.commit()
    print("Seeded accounts: 1 superadmin, 3 admin, 6 user (passwords hashed)")


def seed_events(session: Session):
    if session.exec(select(Event)).first():
        print("Events already seeded")
        return

    events = [
        Event(
            name=f"Event {i}",
            description="Sample event",
            quota=50,
            started_at=now() + timedelta(days=i),
            ended_at=now() + timedelta(days=i + 1),
            created_at=now(),
            updated_at=now(),
        )
        for i in range(1, 11)
    ]

    session.add_all(events)
    session.commit()
    print("Seeded events")


def seed_registrations(session: Session):
    if session.exec(select(Registration)).first():
        print("Registrations already seeded")
        return

    users = session.exec(select(User)).all()
    events = session.exec(select(Event)).all()

    registrations = []
    for i in range(10):
        registrations.append(
            Registration(
                user_id=users[i % len(users)].id,
                event_id=events[i % len(events)].id,
            )
        )

    session.add_all(registrations)
    session.commit()
    print("Seeded registrations")


def seed_logs(session: Session):
    if session.exec(select(Log)).first():
        print("Logs already seeded")
        return

    accounts = session.exec(select(Account)).all()

    logs = []
    for i in range(10):
        acc = accounts[i % len(accounts)]

        logs.append(
            Log(
                account_id=acc.id,
                created_at=now(),
                action="LOGIN",
                ip_address="127.0.0.1",
                user_agent="Seeder Script",
                entity="account",
                entity_id=acc.id,
            )
        )

    session.add_all(logs)
    session.commit()
    print("Seeded logs")


def run():
    with Session(engine) as session:
        print("Start seeding...")

        seed_roles(session)
        seed_users(session)
        seed_accounts(session)
        seed_events(session)
        seed_registrations(session)
        seed_logs(session)

        print("Seeding done!")


if __name__ == "__main__":
    run()