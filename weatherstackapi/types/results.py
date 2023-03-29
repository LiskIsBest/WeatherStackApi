from pydantic import BaseModel


class result(BaseModel):
    """
    API response location lookup section
    https://weatherstack.com/documentation#location_lookup

    name: str - Name of resulting city.
    country: str - Associated country.
    region: str - Name of the resulting region/state/district.
    lon: float - Longitude coordinates of the resulting location.
    lat: float - Latitude coordinates of resulting location.
    timezone_id: str - Timezone ID associated with the resulting location.
    utc_offset: float - UTC offset of the timezone associated with the resulting locatioin.
    """

    name: str
    country: str
    region: str
    lon: float
    lat: float
    timezone_id: str
    utc_offset: float


class Result(BaseModel):
    __root__: list[result]

    class Config:
        allow_arbitrary_types = True
