from datetime import datetime, time

from pydantic import BaseModel, validator


class Current(BaseModel):
    """
    API response current section
    https://weatherstack.com/documentation#query_parameter

    - observation_time: datetime.time - UTC time of when data was collected.
    - temperature: int - Temperature in selected units.
    - weather_code: int - Universal weather condition code associated with the current weather condition.
    - weather_icons: list[str] - List of PNG weather icons associated with the current weather condition.
    - weather_descriptions: list[str] - List of weather description texts associated with the current weather condition.
    - wind_speed: int - Wind speed in selected units.
    - wind_degree: int - Wind degree.
    - wind_dir: str - Wind direction.
    - pressure: int - Air pressure in selected units.
    - precip: int - Precipitation level in selected units.
    - humidity: int - Air humidity level in percentage.
    - cloudcover: int - cloud cover level in percentage.
    - feelslike: int - "Feels like" temperature in selected units.
    - uv_index: int - UV index associated with the current weather condition.
    - visibility: int - Visibility level in selected units.
    """

    observation_time: time
    temperature: int
    weather_code: int
    weather_icons: list[str]
    weather_descriptions: list[str]
    wind_speed: int
    wind_degree: int
    wind_dir: str
    pressure: int
    precip: int
    humidity: int
    cloudcover: int
    feelslike: int
    uv_index: int
    visibility: int

    @validator("observation_time", pre=True)
    def parse_observation_time(cls, value) -> time:
        return datetime.strptime(value, "%I:%M %p").time()

    class Config:
        allow_arbitrary_types = True
        json_encoders = {time: str}
