from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrServiceProfitCenter(Base):
    __tablename__ = 'mtr_service_profit_center'
    is_active = Column(Boolean, default=True, nullable=False)
    service_profit_center_id = Column(Integer, autoincrement=True, primary_key=True)
    service_profit_center_code = Column(String(20),nullable=False, unique=True)
    service_profit_center_description = Column(String(256), nullable=False)