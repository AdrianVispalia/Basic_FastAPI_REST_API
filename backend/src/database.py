from os import environ
import sqlalchemy as _sql
import sqlalchemy.orm as _sql_orm
import sqlalchemy.ext.declarative as _sql_decl


# db parameters from env variables
ip, port = str(environ.get("DB_ENDPOINT")).split(":", maxsplit=1)
username = environ.get("DB_USERNAME")
password = environ.get("DB_PASSWORD")
database = environ.get("DB_NAME")

DATABASE_URL = f"postgres://{username}:{password}@{ip}:{port}/{database}"

# Creating the db con and orm
engine = _sql.create_engine(DATABASE_URL)
SessionLocal = _sql_orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = _sql_decl.declarative_base()

# Function to share the db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
