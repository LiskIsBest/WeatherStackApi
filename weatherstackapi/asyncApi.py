import functools

import httpx
from pydantic import parse_obj_as

from .BaseApi import BaseWeatherStackApi
from .types import Error, Response, Units, Language


class AsyncWeatherApi(BaseWeatherStackApi):
    def __init__(self, access_key: str):
        self.Client = httpx.AsyncClient(timeout=15.0)
        super().__init__(access_key=access_key)

    # TODO copied from losuapi AsyncOsuApi, need to edit request
    def request(func):
        """async http request"""

        @functools.wraps(func)
        async def wrapper(self, *args, **kwargs):
            data = func(self, *args, **kwargs)
            response = await self.Client.request(
                method=data["method"], url=data["url"], params=data["params"]
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

        Available on: All plans

        - location: str - A single location or multiple semicolon seperated location indentifiers.
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
        - Units options:
          - weatherstackwrapper.types.Units.METRIC = "m"
          - weatherstackwrapper.types.Units.FAHRENHEIT = "f"
          - weatherstackwrapper.types.Units.SCIENTIFIC = "s"
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
