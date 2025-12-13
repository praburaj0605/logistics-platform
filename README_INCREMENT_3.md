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
