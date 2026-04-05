from datetime import date, datetime, time
from sqlalchemy.orm import Session

from models.weather import Weather


class WeatherRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, weather: Weather) -> None:
        self.session.add(weather)

    def add_all(self, weather_records: list[Weather]) -> None:
        self.session.add_all(weather_records)

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def get_all(self) -> list[Weather]:
        return self.session.query(Weather).all()

    def get_by_country(self, country: str) -> list[Weather]:
        return (
            self.session.query(Weather)
            .filter(Weather.country == country)
            .all()
        )

    def get_by_country_and_date(self, country: str, target_date: date) -> list[Weather]:
        return (
            self.session.query(Weather)
            .filter(
                Weather.country == country,
                Weather.last_updated >= datetime.combine(target_date, time.min),
                Weather.last_updated <= datetime.combine(target_date, time.max),
            )
            .all()
        )
