from sqlalchemy import Column, Integer, String, Float, DateTime, Time
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)

    country = Column(String)
    location_name = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    last_updated = Column(DateTime)
    sunrise = Column(String)  

    temperature_celsius = Column(Float)
    humidity = Column(Integer)

    wind_kph = Column(Float)
    wind_degree = Column(Integer)
    wind_direction = Column(String)
    gust_kph = Column(Float)
