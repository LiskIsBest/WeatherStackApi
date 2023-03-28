from pydantic import BaseModel

from .historical import Historical, Forecast
from .current import Current
from .location import Location
from .request import Request


class Response(BaseModel):
    request: Request | None
    location: Location | None
    current: Current | None
    forecast: Forecast | None
    historical: Historical | None

    class Config:
        allow_arbitrary_types = True
