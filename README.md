WeatherStackWrapper
---
In development wrapper library for [WeatherStack](https://weatherstack.com/) weather api.

Install
---
```bash
pip install weatherstackwrapper
```
```bash
poetry add weatherstackwrapper
```

Usage
---
```Python
import weatherstackwrapper as wsw

weatherApi = wsw.WeatherApi(access_key)

weatherApi.current(location, units, language)
weatherApi.historical(location, historical_date, hourly, interval, units, language)
```