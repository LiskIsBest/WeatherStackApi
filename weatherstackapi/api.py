import functools

import httpx
from pydantic import parse_obj_as

from .BaseApi import BaseWeatherStackApi
from .types import Error, Response, Units, Language


class WeatherApi(BaseWeatherStackApi):
    def __init__(self, access_key: str):
        self.Client = httpx.Client(timeout=15.0)
        super().__init__(access_key=access_key)

    def request(func):
        """non-async http request"""

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            data = func(self, *args, **kwargs)
            response = self.Client.request(
                method=data["method"],
                url=data["url"],
                params=data["params"],
            ).json()
            if "success" in response:
                return parse_obj_as(type_=Error, obj=response)
            return parse_obj_as(type_=Response, obj=response)

        return wrapper

    @request
    def current(
        self, location: str, units: str | Units = None, language: str | Language = None
    ) -> Response:
        """
        Returns current weather pydantic object
        https://weatherstack.com/documentation#current_weather

        Available on: All plans

        - location: str - A single location or multiple semicolon seperated location indentifiers.
        - units: str | None - One of the unit identifiers. 
          - (default: Metric)
        - language: str | None - Specify a preferred language using its ISO-code. 
          - (default: English)
        ---
        - Location identifiers options:
          - Name: location = "New York"
          - US/Canada/UK zip code: location = "99501"
          - Coordinates(Lat/Lon): location = "40.7831,-73.9712"
          - IP address: location = "153.65.8.20"
          - IP address(Auto-Fetch): location = "fetch:ip"
        ---
        - Units options:
          - weatherstackapi.types.Units.METRIC = "m"
          - weatherstackapi.types.Units.FAHRENHEIT = "f"
          - weatherstackapi.types.Units.SCIENTIFIC = "s"
        ---
        - Language options:
          - See https://weatherstack.com/documentation#language_parameter
        """
        return super().current(location=location, units=units, language=language)

    @request
    def historical(
        self,
        location: str,
        historical_date: str,
        hourly: bool = None,
        interval: int = None,
        units: str | Units = None,
        language: str | Language = None,
    ) -> Response:
        """
        Returns historical weather pydantic object
        https://weatherstack.com/documentation#historical_weather

        Available on: Standard Plan and higher

        - location: str - A single location or multiple semicolon seperated location indentifiers.
        - historical_date: str - A single historical date of multiple semicolo separated date.
          - (example: 2015-01-21 or 2015-01-21:2015-01-22)
        - hourly: bool - True or False depending on whether of not you want the data to be split hourly.
        - interval: int - Defines the hourly intervals.
          - Only available is hourly is set to True. 
          - Default: 3 hour intervals.
        - units: str | None - One of the unit identifiers. (default: Metric)
        - language: str | None - Specify a preferred language using its ISO-code. (default: English)
        ---
        - Location identifiers options:
          - Name: location = "New York"
          - US/Canada/UK zip code: location = "99501"
          - Coordinates(Lat/Lon): location = "40.7831,-73.9712"
          - IP address: location = "153.65.8.20"
          - IP address(Auto-Fetch): location = "fetch:ip"
        ---
        - Interval options:
          - 1
          - 3
          - 6
          - 12 
          - 24
        ---
        - Units options:
          - weatherstackapi.types.Units.METRIC = "m"
          - weatherstackapi.types.Units.FAHRENHEIT = "f"
          - weatherstackapi.types.Units.SCIENTIFIC = "s"
        ---
        - Language options:
          - See https://weatherstack.com/documentation#language_parameter
        """
        return super().historical(
            location=location,
            historical_date=historical_date,
            hourly=hourly,
            interval=interval,
            units=units,
            language=language,
        )

    @request
    def historical_time_series(
        self,
        location: str,
        historical_date_start: str,
        historical_date_end: str,
        hourly: bool = None,
        interval: int = None,
        units: str | Units = None,
        language: str | Language = None,
    ) -> Response:
        return super().historical_time_series(
            location=location,
            historical_date_start=historical_date_start,
            historical_date_end=historical_date_end,
            hourly=hourly,
            interval=interval,
            units=units,
            language=language,
        )

    @request
    def forecast(
        self,
        location: str,
        forecast_days: int,
        hourly: bool = None,
        interval: int = None,
        units: str | Units = None,
        language: str | Language = None,
    ) -> Response:
        return super().forecast(
            location=location,
            forecast_days=forecast_days,
            hourly=hourly,
            interval=interval,
            units=units,
            language=language,
        )
