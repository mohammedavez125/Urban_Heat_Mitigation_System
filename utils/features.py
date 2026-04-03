import pandas as pd

def add_features(df):
    df["datetime"] = pd.to_datetime(df["datetime"])

    df = df.sort_values(["latitude", "longitude", "datetime"])

    # Lag features
    df["temp_lag1"] = df.groupby(["latitude","longitude"])["temperature"].shift(1)
    df["temp_lag2"] = df.groupby(["latitude","longitude"])["temperature"].shift(2)

    # Rolling
    df["temp_rolling_mean_3"] = df.groupby(["latitude","longitude"])["temperature"].transform(
        lambda x: x.rolling(3).mean()
    )

    # Time features
    df["hour"] = df["datetime"].dt.hour
    df["month"] = df["datetime"].dt.month
    df["day_of_week"] = df["datetime"].dt.weekday
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

    return df