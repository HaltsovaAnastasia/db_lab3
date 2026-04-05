from datetime import datetime

from repositories.weather_repository import WeatherRepository


class WeatherService:
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def get_all_weather(self):
        return self.repository.get_all()

    def get_weather_by_country(self, country: str):
        return self.repository.get_by_country(country)

    def get_weather_by_country_and_date(self, country: str, date_str: str):
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return self.repository.get_by_country_and_date(country, target_date)
