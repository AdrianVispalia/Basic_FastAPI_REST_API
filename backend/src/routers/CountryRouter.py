from typing import List
import fastapi as _fastapi
import services as _services
import database as _db
import schemas as _schemas
import sqlalchemy.orm as _orm



router = _fastapi.APIRouter()


@router.get("/", status_code=200, response_model=List[_schemas.CountrySchema])
async def get_countries(
    db: _orm.Session= _fastapi.Depends(_db.get_db),
):
    return await _services.get_countries(db=db)


@router.get("/{country_name}", status_code=200, response_model=_schemas.CountrySchema)
async def get_country(
    country_name: str,
    db: _orm.Session= _fastapi.Depends(_db.get_db),
):
    return await _services.get_country(country_name=country_name, db=db)


@router.post("/", response_model=_schemas.CountrySchema)
async def create_country(
    country_schema: _schemas.CountrySchema,
    db: _orm.Session = _fastapi.Depends(_db.get_db),
):
    print("Trying to create a country!!")
    return await _services.create_country(db=db, country_schema=country_schema)
