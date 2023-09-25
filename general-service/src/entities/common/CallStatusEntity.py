from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCallStatus(Base):
    __tablename__ = 'mtr_call_status'
    is_active = Column(Boolean, default=True, nullable=False)
    call_status_id = Column(Integer, autoincrement=True, primary_key=True)
    call_status_code = Column(String(10), nullable=False, unique=True)
    call_status_description = Column(String(50), nullable=False)
