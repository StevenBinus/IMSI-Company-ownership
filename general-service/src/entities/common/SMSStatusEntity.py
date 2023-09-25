from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSMSStatus(Base):
    __tablename__ = 'mtr_sms_status'
    is_active = Column(Boolean, default=True, nullable=False)
    sms_status_id = Column(Integer, autoincrement=True, primary_key=True)
    sms_status_code = Column(String(20),nullable=False, unique=True)
    sms_status_description = Column(String(256), nullable=False)