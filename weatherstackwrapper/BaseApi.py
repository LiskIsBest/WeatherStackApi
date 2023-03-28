from .types import Units, Language, Response
from .utility import c_TypeError


class BaseWeatherStackApi:
    base_url = "https://api.weatherstack.com/"

    def __init__(self, access_key: str):
        self.__access_key = access_key

    def current(
        self, location: str, units: str | Units = None, language: str | Language = None
    ) -> Response:
        params = {"access_key": self.__access_key}

        if not isinstance(location, str):
            raise c_TypeError(
                param_name="location", correct="str", wrong=type(location).__name__
            )
        params["query"] = location

        if units:
            if isinstance(units, Units):
                units = units.value
            elif not isinstance(units, str):
                raise c_TypeError(
                    param_name="units", correct="str", wrong=type(location).__name__
                )
            params["units"] = units

        if language:
            if isinstance(language, Language):
                language = language.value
            elif not isinstance(units, str):
                raise c_TypeError(
                    param_name="units", correct="str", wrong=type(location).__name__
                )
            params["language"] = language

        return {"method": "GET", "url": self.base_url + "current", "params": params}

    def historical(
        self,
        location: str,
        historical_date: str,
        hourly: bool = None,
        interval: int = None,
        units: str | Units = None,
        language: str | Language = None,
    ) -> Response:
        params = {
            "access_key": self.__access_key,
        }

        if not isinstance(location, str):
            raise c_TypeError(
                param_name="location", correct="str", wrong=type(location).__name__
            )
        params["query"] = location

        if not isinstance(historical_date, str):
            raise c_TypeError(
                param_name="historical_date",
                correct="str",
                wrong=type(location).__name__,
            )
        params["historical_date"] = historical_date

        if hourly:
            if not isinstance(hourly, bool):
                raise c_TypeError(
                    param_name=hourly, correct="bool", wrong=type(hourly).__name
                )
            params["hourly"] = hourly.__int__()

        if interval:
            if not isinstance(interval, int):
                raise c_TypeError(
                    param_name="interval", correct="int", wrong=type(interval).__name__
                )
            params["interval"] = interval

        if units:
            if isinstance(units, Units):
                units = units.value
            elif not isinstance(units, str):
                raise c_TypeError(
                    param_name="units", correct="str", wrong=type(location).__name__
                )
            params["units"] = units

        if language:
            if isinstance(language, Language):
                language = language.value
            elif not isinstance(units, str):
                raise c_TypeError(
                    param_name="units", correct="str", wrong=type(location).__name__
                )
            params["language"] = language

        return {"method": "GET", "url": self.base_url + "historical", "params": params}
