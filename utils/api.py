import requests
from datetime import datetime
import streamlit as st

API_KEY = st.secrets["API_KEY"]

def fetch_weather(name, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    try:
        res = requests.get(url).json()

        if "main" not in res:
            return None

        return {
            "zone": name,
            "datetime": datetime.now(),
            "temperature": res["main"]["temp"],
            "humidity": res["main"]["humidity"],
            "wind_speed": res["wind"]["speed"],
            "latitude": lat,
            "longitude": lon
        }

    except:
        return None