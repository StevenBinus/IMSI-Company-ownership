from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCallFlag(Base):
    __tablename__ = 'mtr_call_flag'
    is_active = Column(Boolean, default=True, nullable=False)
    call_flag_id = Column(Integer, autoincrement=True, primary_key=True)
    call_flag_code = Column(String(10), nullable=False, unique=True)
    call_flag_description = Column(String(50), nullable=False)
