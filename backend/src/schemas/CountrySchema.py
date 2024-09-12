import pydantic as _pydantic


class CountrySchema(_pydantic.BaseModel):
    name: str
    population: int

    class Config:
        orm_mode = True