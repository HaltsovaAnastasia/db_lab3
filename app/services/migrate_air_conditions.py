from app.db import SessionLocal
from app.models.weather import Weather
from app.models.air_conditions import AirConditions


def should_go_outside_rule(condition, humidity, visibility_km, uv_index):
    bad_words = ["rain", "drizzle", "storm", "fog", "snow", "blizzard", "thunder"]

    condition_lower = (condition or "").lower()

    if humidity is not None and humidity > 85:
        return False
    if visibility_km is not None and visibility_km < 2:
        return False
    if uv_index is not None and uv_index > 8:
        return False
    if any(word in condition_lower for word in bad_words):
        return False

    return True


def migrate_air_conditions():
    session = SessionLocal()

    try:
        weather_rows = session.query(Weather).all()

        for row in weather_rows:
            exists = session.query(AirConditions).filter_by(weather_id=row.id).first()
            if exists:
                continue

            air = AirConditions(
                weather_id=row.id,
                humidity=row.humidity,
                visibility_km=row.visibility_km,
                pressure_mb=row.pressure_mb,
                uv_index=row.uv_index,
                condition=row.condition,
                should_go_outside=should_go_outside_rule(
                    row.condition,
                    row.humidity,
                    row.visibility_km,
                    row.uv_index,
                ),
            )
            session.add(air)

        session.commit()
        print("Дані успішно перенесено в air_conditions.")
    except Exception as e:
        session.rollback()
        print(f"Помилка під час переносу: {e}")
    finally:
        session.close()
