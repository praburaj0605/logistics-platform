# Increment 5 – Vendors & Rate Cards

## What this adds
- Vendors CRUD
- Rate cards per vendor
- JWT-protected endpoints
- DB migrations

## Endpoints
POST /vendors
GET  /vendors

POST /ratecards
GET  /ratecards

## How to run
1. docker-compose build backend
2. docker-compose exec backend alembic upgrade head
3. Include routers in main.py
