import concurrent
import requests
import streamlit as st
import pandas as pd
from db import insert_weather
import requests

API_KEY = st.secrets["API_KEY"]
def fetch_weather(zone, lat, lon):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return None

        return {
            "zone": zone,
            "latitude": lat,
            "longitude": lon,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    except:
        return None

