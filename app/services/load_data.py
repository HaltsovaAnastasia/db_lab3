import pandas as pd
from datetime import datetime
from app.db import SessionLocal
from app.models.weather import Weather


def parse_datetime(value):
    if pd.isna(value):
        return None
    try:
        return pd.to_datetime(value)
    except:
        return None


def parse_time(value):
    if pd.isna(value):
        return None
    try:
        return datetime.strptime(str(value), "%I:%M %p").time()
    except:
        try:
            return pd.to_datetime(value).time()
        except:
            return None


def load_csv():
    df = pd.read_csv("GlobalWeatherRepository.csv")

    session = SessionLocal()

    try:
        for _, row in df.iterrows():
            weather = Weather(
                country=row.get("country"),
                wind_degree=row.get("wind_degree"),
                wind_kph=row.get("wind_kph"),
                wind_direction=row.get("wind_direction"),
                last_updated=parse_datetime(row.get("last_updated")),
                sunrise=parse_time(row.get("sunrise")),
                humidity=row.get("humidity"),
                visibility_km=row.get("visibility_km"),
                pressure_mb=row.get("pressure_mb"),
                uv_index=row.get("uv_index"),
                condition=row.get("condition_text"),
            )

            session.add(weather)

        session.commit()
        print("Дані успішно завантажено!")

    except Exception as e:
        session.rollback()
        print("Помилка:", e)

    finally:
        session.close()
