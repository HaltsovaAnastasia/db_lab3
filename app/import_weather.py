from pathlib import Path
import pandas as pd

from database import SessionLocal
from models.weather import Weather
from repositories.weather_repository import WeatherRepository


def main():
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "GlobalWeatherRepository.csv"

    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        return

    print("Reading CSV file...")
    df = pd.read_csv(csv_path)

    # Temporary limit for testing (remove in final version)
    df = df.head(1000)

    session = SessionLocal()
    repository = WeatherRepository(session)

    try:
        print("Importing data into database...")

        weather_records = []

        for _, row in df.iterrows():
            weather = Weather(
                country=row["country"],
                location_name=row["location_name"],
                latitude=row["latitude"],
                longitude=row["longitude"],
                last_updated=pd.to_datetime(row["last_updated"]),
                sunrise=row["sunrise"],
                temperature_celsius=row["temperature_celsius"],
                humidity=row["humidity"],
                wind_kph=row["wind_kph"],
                wind_degree=row["wind_degree"],
                wind_direction=row["wind_direction"],
                gust_kph=row["gust_kph"],
            )
            weather_records.append(weather)

        repository.add_all(weather_records)
        repository.commit()

        print("Import completed successfully.")

    except Exception as e:
        repository.rollback()
        print("Error during import:")
        print(e)

    finally:
        session.close()


if __name__ == "__main__":
    main()
