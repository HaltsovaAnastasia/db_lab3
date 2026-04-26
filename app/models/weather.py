from sqlalchemy import Column, Integer, String, Float, DateTime, Time
from app.db import Base


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)

    country = Column(String(100), nullable=True)

    wind_degree = Column(Integer, nullable=True)
    wind_kph = Column(Float, nullable=True)
    wind_direction = Column(String(20), nullable=True)

    last_updated = Column(DateTime, nullable=True)
    sunrise = Column(Time, nullable=True)

    humidity = Column(Integer, nullable=True)
    visibility_km = Column(Float, nullable=True)
    pressure_mb = Column(Float, nullable=True)
    uv_index = Column(Float, nullable=True)
    condition = Column(String(100), nullable=True)
