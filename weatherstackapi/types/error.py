from pydantic import BaseModel, Field


class error(BaseModel):
    code: int
    Type: str = Field(alias="type")
    info: str


class Error(BaseModel):
    success: bool
    error: error

    class Config:
        allow_arbitrary_types = True
