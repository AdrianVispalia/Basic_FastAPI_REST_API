'''Database model'''
import sqlalchemy as _sql
import database as _db


class CountryModel(_db.Base):
    '''Country object model for the database'''
    __tablename__ = "countries"
    name = _sql.Column(_sql.String, primary_key=True, index=True)
    population = _sql.Column(_sql.Integer, nullable=False)
