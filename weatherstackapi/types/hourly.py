from pydantic import BaseModel


class Hourly(BaseModel):
    """
    API historical/forecast response hourly section
    https://weatherstack.com/documentation#historical_weather

    - time: int - Time as a number in 24h format. EX: 3:00pm -> 1500
    - temperature: int - Temperature in selected units.
    - wind_speed: int - Wind speed in selected units.
    - wind_degree: int - Wind degree.
    - wind_dir: str - Wind direction.
    - weather_code: int - Univeral weather condition code.
    - weather_icons: list[str] - List of PNG weather icons.
    - weather_descriptions: list[str] - List of weather descriptions.
    - precip: float - Precipitation level in selected units.
    - humidity: int - Air humidity level in percentage.
    - visibility: int - Visibility level in selected units.
    - pressure: int - Air pressure in selected units.
    - cloudcover: int - Cloud cover level in percentage.
    - heatindex: int - Heat index temperature in selected units.
    - dewpoint: int - Dew point temperatur in selected units.
    - windchill: int - Wind chill temperature in selected units.
    - windgust: int - Wind gust speed in selected units.
    - feelslike: int - "Feels like" temperature in selected units.
    - chanceofrain: int - Chance of rain in percentage.
    - chanceofremdry: int - Change of remaining dry in percentage.
    - chanceofwindy: int - Chance of being windy in percentage.
    - chanceofovercast: int - Chance of being overcast in percentage.
    - chanceofsunshine: int - Chance of sunshine in percentage.
    - chanceoffrost: int - Chance of frost in percentage.
    - chanceofhightemp: int - Chance of high temperatures in percentage.
    - chanceoffog: int - Chance of fog in percentage.
    - chanceofsnow: int - Chance of snow in percentage.
    - chanceofthunder: int - chance of thunder in percentage.
    - uv_index: int - UV index associated with the current weather condition.
    """

    time: int
    temperature: int
    wind_speed: int
    wind_degree: int
    wind_dir: str
    weather_code: int
    weather_icons: list[str]
    weather_descriptions: list[str]
    precip: float
    humidity: int
    visibility: int
    pressure: int
    cloudcover: int
    heatindex: int
    dewpoint: int
    windchill: int
    windgust: int
    feelslike: int
    chanceofrain: int
    chanceofremdry: int
    chanceofwindy: int
    chanceofovercast: int
    chanceofsunshine: int
    chanceoffrost: int
    chanceofhightemp: int
    chanceoffog: int
    chanceofsnow: int
    chanceofthunder: int
    uv_index: int
