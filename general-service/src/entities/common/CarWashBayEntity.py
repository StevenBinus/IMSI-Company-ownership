from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCarWashBay(Base):
    __tablename__ = 'mtr_car_wash_bay'
    is_active = Column(Boolean, default=True, nullable=False)
    car_wash_bay_id = Column(Integer, autoincrement=True, primary_key=True)
    car_wash_bay_code = Column(String(10), nullable=False, unique=True)
    car_wash_bay_description = Column(String(50), nullable=False)
