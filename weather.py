import requests
import pandas as pd
from datetime import date

# My camping location
LATITUDE = 36.0566
LONGITUDE = -112.1251
LOCATION_NAME = "Grand Canyon"

# Camping month and day range
CAMP_MONTH = 10
CAMP_START_DAY = 1
CAMP_END_DAY = 14

def get_historical_weather(lat, lon, start_date, end_date):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "America/Los_Angeles"
    }
    response = requests.get(url, params=params)
    return response.json()
