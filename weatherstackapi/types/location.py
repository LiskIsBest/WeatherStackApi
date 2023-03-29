from datetime import datetime

from pydantic import BaseModel, validator


class Location(BaseModel):
    """
    API response location section - https://weatherstack.com/documentation#query_parameter

    - name: str - Name of location used.
    - country: str - Country name associated with the location used.
    - region: str - Region name associated with the loaction used.
    - lat: float - Latitude coordinate associated with the location used.
    - lon: float - Longitude coordinate associated with the location used.
    - timezone_id: str - Timezone ID associated with the location used.
    - localtime: datetime.datetime - Local time of the location used.
    - localtime_epoch: int - Local time as UNIX timestamp of the laction used.
    - utc_offset: float - UTC offset of the timezone of the location used.
    """

    name: str
    country: str
    region: str
    lat: float
    lon: float
    timezone_id: str
    localtime: datetime
    localtime_epoch: int
    utc_offset: float

    @validator("localtime", pre=True)
    def parse_localtime(cls, value) -> datetime:
        """formats given string timestamp to datetime object"""
        return datetime.strptime(value, "%Y-%m-%d %H:%M")

    class Config:
        allow_arbitrary_types = True
        json_encoders = {datetime: str, float: str}
