from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrRecordStatus(Base):
    __tablename__ = 'mtr_record_status'
    is_active = Column(Boolean, default=True, nullable=False)
    record_status_id = Column(Integer, autoincrement=True, primary_key=True)
    record_status_code = Column(String(20),nullable=False, unique=True)
    record_status_description = Column(String(256), nullable=False)