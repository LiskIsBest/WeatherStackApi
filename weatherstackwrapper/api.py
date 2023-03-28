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
