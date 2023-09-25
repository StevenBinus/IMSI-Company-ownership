from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCarWashStatus(Base):
    __tablename__ = 'mtr_car_wash_status'
    is_active = Column(Boolean, default=True, nullable=False)
    car_wash_status_id = Column(Integer, autoincrement=True, primary_key=True)
    car_wash_status_code = Column(String(10), nullable=False, unique=True)
    car_wash_status_description = Column(String(50), nullable=False)
