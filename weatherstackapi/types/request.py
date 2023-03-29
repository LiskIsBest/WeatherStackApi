from pydantic import BaseModel, Field


class Request(BaseModel):
    """
    API response request section
    https://weatherstack.com/documentation#query_parameter

    - Type: str - Type of location lookup used. ("City", "LatLon", "IP", "Zipcode")
    - query: str - Exact location identifier.
    - language: str - ISO-Code of the language used.
    - unit: str - Unit identifier used. ("m","s","f")
    - results: int - Count of results.
    """

    Type: str | None = Field(alias="type")
    query: str | None
    language: str | None
    unit: str | None
    results: int | None
