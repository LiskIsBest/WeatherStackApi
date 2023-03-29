from datetime import datetime, time

from pydantic import BaseModel, validator


class Astro(BaseModel):
    """
    API historical response astro section - https://weatherstack.com/documentation#historical_weather

    time format: hh:mm:ss 24 hour clock

    - sunrise: datetime.time - Local sunrise time.
    - sunset: datetime.time - Local sunset time.
    - moonrise: datetime.time - Local moonrise time.
    - moonset: datetime.time - Local moonset time.
    - moon_phase: str - Local moon phase.
    - moon_illumination: int - Moon illumination level as percentage.
    """

    sunrise: time
    sunset: time
    moonrise: time
    moonset: time
    moon_phase: str
    moon_illumination: int

    @validator("sunrise", pre=True)
    def parse_sunrise(cls, value) -> time:
        if value == "No sunrise":
            return datetime.strptime("12:00 AM", "%I:%M %p").time()
        return datetime.strptime(value, "%I:%M %p").time()

    @validator("sunset", pre=True)
    def parse_sunset(cls, value) -> time:
        if value == "No sunset":
            return datetime.strptime("12:00 AM", "%I:%M %p").time()
        return datetime.strptime(value, "%I:%M %p").time()

    @validator("moonrise", pre=True)
    def parse_moonrise(cls, value) -> time:
        if value == "No moonrise":
            return datetime.strptime("12:00 AM", "%I:%M %p").time()
        return datetime.strptime(value, "%I:%M %p").time()

    @validator("moonset", pre=True)
    def parse_moonset(cls, value) -> time:
        if value == "No moonset":
            return datetime.strptime("12:00 AM", "%I:%M %p").time()
        return datetime.strptime(value, "%I:%M %p").time()

    class Config:
        allow_arbitrary_types = True
        json_encoders = {time: str}
