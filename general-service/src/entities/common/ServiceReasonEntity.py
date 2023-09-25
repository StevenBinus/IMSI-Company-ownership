from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrServiceReason(Base):
    __tablename__ = 'mtr_service_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    service_reason_id = Column(Integer, autoincrement=True, primary_key=True)
    service_reason_code = Column(String(5),nullable=False, unique=True)
    service_reason_description = Column(String(50), nullable=False)