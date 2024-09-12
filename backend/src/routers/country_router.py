'''Endpoints and HTTP logic'''
from typing import List
import fastapi as _fastapi
import services as _services
import database as _db
import schemas as _schemas
import sqlalchemy.orm as _orm


router = _fastapi.APIRouter()


@router.post("/", response_model=_schemas.CountrySchema)
async def create_country(
    country_schema: _schemas.CountrySchema,
    db: _orm.Session = _fastapi.Depends(_db.get_db),
):
    '''Create country endpoint, returns a CountrySchema'''
    try:
        country = await _services.create_country(db=db, country_schema=country_schema)
    except _services.ItemException as ex:
        raise _fastapi.HTTPException(status_code=ex.http_code, detail=str(ex))

    return country


@router.get("/{country_name}", status_code=200, response_model=_schemas.CountrySchema)
async def get_country(
    country_name: str,
    db: _orm.Session= _fastapi.Depends(_db.get_db),
):
    '''Get country endpoint, returns a CountrySchema'''
    try:
        country = await _services.get_country(country_name=country_name, db=db)
    except _services.ItemException as ex:
        raise _fastapi.HTTPException(status_code=ex.http_code, detail=str(ex))

    return country


@router.get("/", status_code=200, response_model=List[_schemas.CountrySchema])
async def get_countries(
    db: _orm.Session= _fastapi.Depends(_db.get_db),
):
    '''Get countries endpoint, returns a list of CountrySchema'''
    return await _services.get_countries(db=db)
