# Increment 2 – Database Schema & Alembic

## What this adds
- SQLAlchemy Base and DB session
- Core models: Client, Enquiry
- Alembic configuration
- Initial migration

## How to test
1. docker-compose up -d
2. make migrate
3. docker-compose exec postgres psql -U logistics -d logistics
   \dt
