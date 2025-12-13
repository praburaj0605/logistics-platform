# Increment 1 – Environment & Folder Architecture

## What this increment provides
- Docker Compose dev environment
- Backend (FastAPI) container
- Frontend (React + Vite) container
- Postgres database
- MinIO (S3-compatible storage)
- Makefile shortcuts

## How to run
1. Copy env file
   cp .env.example .env

2. Start stack
   make up

3. Access services
- Backend: http://localhost:8000/health
- Frontend: http://localhost:5173
- MinIO Console: http://localhost:9001

## Next increment
Increment 2 will introduce database models and Alembic migrations.
