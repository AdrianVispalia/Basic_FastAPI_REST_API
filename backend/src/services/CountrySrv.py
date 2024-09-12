import sqlalchemy.orm as _orm
import models as _models
import schemas as _schemas


async def create_country(country_schema: _schemas.CountrySchema, db: _orm.Session):
    db.add(_models.CountryModel(**country_schema.dict()))
    db.commit()
    db.refresh(country_schema)
    return _schemas.CountrySchema.from_orm(country_schema)


async def get_country(country_name: str, db: _orm.Session):
    query = db.query(_models.CountryModel).filter(_models.CountryModel.name == country_name)
    return query.first() if query is not None else None


async def get_countries(db: _orm.Session):
    countries = db.query(_models.CountryModel)
    return list(map(_schemas.CountrySchema.from_orm, countries))
