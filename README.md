# 🧑‍💼 User Management System API

A secure and scalable User Management System built with **FastAPI**, using **JWT-based authentication**, modular routing, and containerized with **Docker**. Supports user registration, login, token handling, and more.

---

## 📁 Project Structure

user-management-system/
│

├── app/

│ ├── init.py # Package initializer

│ ├── main.py # FastAPI app entry point

│ ├── models.py # 

│ ├── schema.py # 

│ ├── routes/ # API routes

│ ├── config.py # Settings and environment variables

│ ├── oauth2.py # OAuth2 password flow logic

│ ├── jwt_token_module.py # JWT token creation & decoding

│ ├── hashing.py # Password hashing utilities

| ├── requirements.txt # Python dependencies

| ├── Dockerfile # Docker configuration

| | ── docker-compose.yml # Docker services and DB setup


## Features

-  User registration & login
-  Secure password hashing (bcrypt)
-  JWT-based authentication
-  Role-based token generation (optional)
-  Modular routing and clean code structure
-  Environment-based configuration
-  Dockerized deployment with `docker-compose`

##Tech Stack

- **FastAPI** - High-performance web framework
- **Pydantic** - Data validation
- **MongoDB** - ORM for DB operations
- **JWT (PyJWT)** - Secure token-based authentication
- **Docker + Compose** - Containerization
- **bcrypt** - Password hashing


docker-compose up --build (App will be available at-> http://localhost:8000)

Environment Variables
Update environment variables in .env or config.py (or pass them via Docker):

DATABASE_URL – DB connection URL

SECRET_KEY – for JWT signing

ALGORITHM – hashing algorithm (e.g., HS256)

ACCESS_TOKEN_EXPIRE_MINUTES – token lifetime
