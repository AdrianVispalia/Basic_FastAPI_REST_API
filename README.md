# README

Basic FastAPI countries REST API.

## Installation

```bash
docker-compose build
docker-compose up -d

python3 test.py
```

## Useful links

- Redoc: `http://localhost:8000/redoc`
- OpenAPI (Swagger): `http://localhost:8000/docs`

## Folder structure

```bash
- main.py # FastAPI settings
- database.py # database connection settings
- models/  # database objects models
  |- country_model.py # country database object model
- schemas/ # JSON schemas
  |- country_schema # country JSON schema
- routers/ # endpoints + basic business logic
  |- country_router.py # countries endpoints
- services/
  |- country_srv.py # country services (CRUD)
  |- custom_exceptions.py # Custom CRUD exceptions
```