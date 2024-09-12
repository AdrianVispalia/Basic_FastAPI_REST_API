'''JSON schema'''
import pydantic as _pydantic


class CountrySchema(_pydantic.BaseModel):
    '''Country object schema for JSON'''
    name: str
    population: int

    class Config:
        '''Required for ORM'''
        orm_mode = True
