# RSI Tugas Praktikum 2

Backend API project built using FastAPI, SQLModel, Alembic, and PostgreSQL with Docker.

---

## Tech Stack

* FastAPI
* SQLModel
* Alembic (Database Migration)
* PostgreSQL (Docker)
* Uvicorn

---

## Setup and Installation

### 1. Clone Repository

```bash
git clone https://github.com/T-Rex2586/RSI-TugasPrak2.git
cd RSI-TugasPrak2
```

---

### 2. Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install "fastapi[standart]", uvicorn, sqlmodel, psycopg2, alembic, "python-jose[cryptography]" "passlib[bcrypt]"
```

---

## Database Setup (Docker)

### 1. Reset Database (Optional)

```bash
docker-compose down -v
```

Remove existing data directory:

```bash
rm -rf data
```

---

### 2. Start PostgreSQL Container

```bash
docker-compose up -d
```

---

### 3. Access PostgreSQL

```bash
docker exec -it docker-rsi psql -U postgres
```

---

### 4. Create Database

```sql
CREATE DATABASE acara_rsi;
```

Exit:

```sql
\q
```

---

## Database Migration

Apply migrations using Alembic:

```bash
alembic upgrade head
```

---

## Seeding Initial Data

Populate the database with initial data:

```bash
python -m src.seed
```

---

## Run Application

```bash
uvicorn src.app:app --reload
```

Application will be available at:

```
http://127.0.0.1:8000
```

---

## Project Structure

```
src/
├── app.py
├── seed.py
├── database/
├── controllers/
├── services/
├── repositories/
├── routes/
```

---

## Notes

* Ensure Docker is running before starting the project
* Seeder is designed to avoid duplicate data
* Use `docker-compose down -v` to reset the database completely

---

## Development Workflow

Generate migration after model changes:

```bash
alembic revision --autogenerate -m "message"
```

Apply migration:

```bash
alembic upgrade head
```

---

## Author

Kelompok 1 Kelas A

---
