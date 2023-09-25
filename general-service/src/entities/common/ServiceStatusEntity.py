from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrServiceStatus(Base):
    __tablename__ = 'mtr_service_status'
    is_active = Column(Boolean, default=True, nullable=False)
    service_status_id = Column(Integer, autoincrement=True, primary_key=True)
    service_status_code = Column(String(20),nullable=False, unique=True)
    service_status_description = Column(String(256), nullable=False)