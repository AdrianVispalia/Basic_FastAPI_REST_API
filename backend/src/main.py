'''FastAPI configuration'''
import fastapi as _fastapi
import routers as _routers
import database as _db


app = _fastapi.FastAPI()


app.include_router(_routers.country_router.router, prefix="/api/v1/data/countries")


@app.get("/api/v1/create")
async def database_creation():
    '''Function that creates the db tables from the models'''
    _db.Base.metadata.create_all(bind=_db.engine)
    return {"message": "Created database scheme"}
