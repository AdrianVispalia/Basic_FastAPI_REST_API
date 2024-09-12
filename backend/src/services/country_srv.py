'''CRUD logic operations'''
import sqlalchemy.orm as _orm
import models as _models
import schemas as _schemas
from .custom_exceptions import ItemAlreadyExistsException, ItemDoesNotExistException


async def create_country(country_schema: _schemas.CountrySchema, db: _orm.Session):
    '''Create country function. It will not work if an entry already exists in the db'''
    query = db.query(_models.CountryModel).filter(_models.CountryModel.name == country_schema.name)
    if query.first() is not None:
        raise ItemAlreadyExistsException()

    db.add(_models.CountryModel(**country_schema.dict()))
    db.commit()
    db.refresh(country_schema)
    return _schemas.CountrySchema.from_orm(country_schema)



async def get_country(country_name: str, db: _orm.Session):
    '''Get country function. It will return None if it doesn't exist'''
    query = db.query(_models.CountryModel).filter(_models.CountryModel.name == country_name)
    if query.first() is None:
        raise ItemDoesNotExistException()

    return query.first()


async def get_countries(db: _orm.Session):
    '''Get countries function. It will return an empty list if there are no countries'''
    countries = db.query(_models.CountryModel)
    return list(map(_schemas.CountrySchema.from_orm, countries))
