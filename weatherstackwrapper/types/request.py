from pydantic import BaseModel, Field


class Request(BaseModel):
    """
    API response request section - https://weatherstack.com/documentation#query_parameter

    - Type: str - Type of location lookup used. ("City", "LatLon", "IP", "Zipcode")
    - query: str - Exact location identifier.
    - language: str - ISO-Code of the language used.
    - unit: str - Unit identifier used. ("m","s","f")
    """

    Type: str = Field(alias="type")
    query: str
    language: str
    unit: str
