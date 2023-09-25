from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrPeriodStatus(Base):
    __tablename__ = 'mtr_period_status'
    is_active = Column(Boolean, default=True, nullable=False)
    period_status_id = Column(Integer, autoincrement=True, primary_key=True)
    period_status_code = Column(String(5),nullable=False, unique=True)
    period_status_description = Column(String(50), nullable=False)