from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class AirConditions(Base):
    __tablename__ = "air_conditions"

    id = Column(Integer, primary_key=True, index=True)
    weather_id = Column(Integer, ForeignKey("weather.id"), nullable=False, unique=True)

    humidity = Column(Integer, nullable=True)
    visibility_km = Column(Float, nullable=True)
    pressure_mb = Column(Float, nullable=True)
    uv_index = Column(Float, nullable=True)
    condition = Column(String(100), nullable=True) 

    should_go_outside = Column(Boolean, nullable=True)
