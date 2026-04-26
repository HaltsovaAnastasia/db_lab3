from sqlalchemy import func
from datetime import datetime
from app.db import SessionLocal
from app.models.weather import Weather
from app.models.air_conditions import AirConditions


def get_weather_by_country_and_date(country: str, date_str: str):
    session = SessionLocal()

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        results = (
            session.query(Weather, AirConditions)
            .join(AirConditions, AirConditions.weather_id == Weather.id)
            .filter(func.lower(Weather.country) == country.lower())
            .filter(func.date(Weather.last_updated) == date_obj)
            .all()
        )

        return results

    finally:
        session.close()
