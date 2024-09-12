import sqlalchemy as _sql
import database as _db

class CountryModel(_db.Base):
    __tablename__ = "countries"
    name = _sql.Column(_sql.String, primary_key=True, index=True)
    population = _sql.Column(_sql.Integer, nullable=False)
