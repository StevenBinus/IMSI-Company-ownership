from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFareType(Base):
    __tablename__ = 'mtr_fare_type'
    is_active = Column(Boolean, default=True, nullable=False)
    fare_type_id = Column(Integer, autoincrement=True, primary_key=True)
    fare_type_code = Column(String(10), nullable=False, unique=True)
    fare_type_description = Column(String(50), nullable=False)