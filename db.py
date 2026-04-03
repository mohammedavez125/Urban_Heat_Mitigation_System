import sqlite3
from datetime import datetime
import pandas as pd

DB_NAME = "urban_heat.db"

# ==============================
# INIT DB (UPDATED)
# ==============================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Locations table
    c.execute("""
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        latitude REAL,
        longitude REAL
    )
    """)

    # Weather history table (UPDATED)
    c.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        zone TEXT,
        datetime TEXT,
        latitude REAL,
        longitude REAL,
        temperature REAL,
        humidity REAL,
        wind_speed REAL
    )
    """)

    conn.commit()
    conn.close()


# ==============================
# INSERT LOCATION
# ==============================
def insert_location(name, lat, lon):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT OR IGNORE INTO locations (name, latitude, longitude)
    VALUES (?, ?, ?)
    """, (name, lat, lon))

    conn.commit()
    conn.close()


# ==============================
# GET LOCATIONS
# ==============================
def get_locations():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT name, latitude, longitude FROM locations")
    rows = c.fetchall()

    conn.close()

    if not rows:
        return {}

    return {r[0]: (r[1], r[2]) for r in rows}


# ==============================
# INSERT WEATHER (UPDATED)
# ==============================
def insert_weather(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT INTO weather_data
    (zone, datetime, latitude, longitude, temperature, humidity, wind_speed)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["zone"],  # 🔥 IMPORTANT
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data["latitude"],
        data["longitude"],
        data["temperature"],
        data["humidity"],
        data["wind_speed"]
    ))

    conn.commit()
    conn.close()


# ==============================
# GET HISTORY (FOR UI)
# ==============================
def get_history(zone):
    conn = sqlite3.connect(DB_NAME)

    query = """
    SELECT temperature, humidity, wind_speed, datetime
    FROM weather_data
    WHERE zone = ?
    ORDER BY datetime ASC
    """

    df = pd.read_sql(query, conn, params=(zone,))
    conn.close()

    return df


# ==============================
# GET COMPLETE HISTORY
# ==============================
def get_complete_history():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql("SELECT * FROM weather_data", conn)
    conn.close()

    return df