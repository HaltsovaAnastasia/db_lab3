from database import SessionLocal
from repositories.weather_repository import WeatherRepository
from services.weather_service import WeatherService

def print_weather_records(records):
    if not records:
        print("No weather records found.")
        return

    print(f"\nFound {len(records)} record(s):\n")

    for record in records:
        print(f"Country: {record.country}")
        print(f"Location: {record.location_name}")
        print(f"Latitude: {record.latitude}")
        print(f"Longitude: {record.longitude}")
        print(f"Last updated: {record.last_updated}")
        print(f"Sunrise: {record.sunrise}")
        print(f"Temperature (C): {record.temperature_celsius}")
        print(f"Humidity: {record.humidity}")
        print(f"Wind (kph): {record.wind_kph}")
        print(f"Wind degree: {record.wind_degree}")
        print(f"Wind direction: {record.wind_direction}")
        print(f"Gust (kph): {record.gust_kph}")
        print("-" * 40)


def main():
    session = SessionLocal()
    repository = WeatherRepository(session)
    service = WeatherService(repository)

    try:
        print("Weather search")
        print("Enter search parameters below.\n")

        country = input("Country: ").strip()
        date_str = input("Date (YYYY-MM-DD): ").strip()

        records = service.get_weather_by_country_and_date(country, date_str)
        print_weather_records(records)

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        print("An error occurred:")
        print(e)
    finally:
        session.close()


if __name__ == "__main__":
    main()
