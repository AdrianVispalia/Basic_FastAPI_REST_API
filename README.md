# README

Basic FastAPI countries REST API.

## Installation

```bash
docker-compose build
docker-compose up -d

python3 test.py
```

## Useful links

- Redoc: `https://localhost:8000/redoc`
- OpenAPI (Swagger): `https://localhost:8000/docs`

## Folder structure

```bash
- main.py # router settings + FastAPI settings
- database.py # database connection settings
- models/  # database objects models
  |- CountryModel.py # country database object model
- schemas/ # JSON schemas
  |- CountrySchema # country JSON schema
- routers/ # endpoints + basic business logic
  |- CountrySchema.py # countries endpoints
- services/
  |- CountrySrv.py # country services (CRUD)
```