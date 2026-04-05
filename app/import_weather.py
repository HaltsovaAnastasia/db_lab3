from pathlib import Path
import pandas as pd

from database import SessionLocal
from models.weather import Weather


def main():
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "GlobalWeatherRepository.csv"

    if not csv_path.exists():
        print(f"File wasn't found': {csv_path}")
        return

    print("Reading CSV...")
    df = pd.read_csv(csv_path)

    df = df.head(1000) #change later

    session = SessionLocal()

    try:
        print("Import to database...")

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
            session.add(weather)

        session.commit()
        print("Success.")

    except Exception as e:
        session.rollback()
        print("Error during import:")
        print(e)

    finally:
        session.close()


if __name__ == "__main__":
    main()
