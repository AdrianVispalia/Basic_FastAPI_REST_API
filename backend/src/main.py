import fastapi as _fastapi
import routers as _routers
import database as _db


app = _fastapi.FastAPI()


app.include_router(_routers.CountryRouter.router, prefix="/api/v1/data/countries")


@app.get("/api/v1/create")
async def database_creation():
    _db.Base.metadata.create_all(bind=_db.engine)
    return {"message": "Created database scheme"}
