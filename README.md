# Logistics Platform

This repository contains the logistics management platform.

## Overview
Incremental development approach.
Increment 0 focuses on repository scaffolding, contribution rules, and CI placeholders.

## Branch Strategy
- main (protected)
- develop
- feature branches: feat/<short-description>

## Getting Started
Detailed setup instructions will be added in Increment 1.

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
# Increment 3 – Authentication & Users

## What this adds
- Users table
- Password hashing (bcrypt)
- JWT authentication
- Auth routes: /auth/register, /auth/login

## How to run
1. Rebuild backend
   docker-compose build backend

2. Run migration
   docker-compose exec backend alembic upgrade head

3. Test auth
POST /auth/register
POST /auth/login

## Notes
- JWT secret is read from SECRET_KEY env variable
- This increment is fully additive (no overwrites)

# Increment 4 – Clients CRUD (JWT Protected)

## What this adds
- Client CRUD API
- JWT-protected routes

## Endpoints
POST   /clients
GET    /clients
GET    /clients/{id}
DELETE /clients/{id}

## Usage
Authorization header:
Authorization: Bearer <access_token>

No new migrations required.

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

# Increment 6 – Quotation Engine

## What this adds
- Quote generation engine
- Route-based rate lookup
- Quote persistence
- JWT-protected quote API

## Endpoint
POST /quotes

## How it works
Client + origin + destination + service
→ rate card lookup
→ final quote stored

## Next
Increment 7 – Orders & Shipments

# Increment 7 – Orders & Shipments

## What this adds
- Convert quotes into orders
- Auto-create shipments
- Tracking number generation
- JWT-protected APIs

## Endpoints
POST /orders
GET  /shipments

## Flow
Quote → Order → Shipment

## Next
Increment 8 – Tracking & Status updates
