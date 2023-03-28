from datetime import datetime, time, date
from typing import Dict

from pydantic import BaseModel, validator

from .astro import Astro
from .hourly import Hourly


class historical_forecast(BaseModel):
    """
    API historical/forecast response - https://weatherstack.com/documentation#historical_weather

    - date: datetime.date - Requested date.
    - date_epoch: int - Requested date as UNIX timestamp.
    - astro: types.Astro - 6 sub response objects containing astronomical weather details.
    - mintemp: int - Minimum temperature of the day in selected units.
    - maxtemp: int - Maximum temperature of the day in selected units.
    - avgtemp: int - Average temperature of the day in selected units.
    - totalsnow: int - Snow fall amount in selected units.
    - sunhour: float - Number of sun hours.
    - uv_index: int - UV index associated with the current weather condition.
    - hourly: list[types.Hourly] - Sub response objects containing hourly weather data.
    """

    date: date
    date_epoch: int
    astro: Astro
    mintemp: int
    maxtemp: int
    avgtemp: int
    totalsnow: int
    sunhour: float
    uv_index: int
    hourly: list[Hourly] | None

    @validator("date", pre=True)
    def parse_date(cls, value) -> datetime:
        """formats given string timestamp to datetime object"""
        return datetime.strptime(value, "%Y-%m-%d")

    class Config:
        allow_arbitrary_types = True
        json_encoders = {date: str, float: str}


class Historical(BaseModel):
    __root__: Dict[str, historical_forecast]

    class Config:
        allow_arbitrary_types = True


class Forecast(BaseModel):
    __root__: Dict[str, historical_forecast]

    class Config:
        allow_arbitrary_types = True
