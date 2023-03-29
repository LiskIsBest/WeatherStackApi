WeatherStackWrapper
---
In development wrapper library for [WeatherStack](https://weatherstack.com/) weather api.

Install
---
```bash
pip install weatherstackapi
```
```bash
poetry add weatherstackapi
```

Usage
---
```Python
import weatherstackapi as wsa

weatherApi = wsa.WeatherApi(access_key)

weatherApi.current(location, units, language)
weatherApi.historical(location, historical_date, hourly, interval, units, language)
weatherApi.historical_time_series(locatioin, historical_date_start, historical_date_end, hourly, interval, units, language)
weatherApi.forecast(location, forecast_days, hourly, interval, units, language)
weatherApi.lookup_location(location)
```