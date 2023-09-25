from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCallMethod(Base):
    __tablename__ = 'mtr_call_method'
    is_active = Column(Boolean, default=True, nullable=False)
    call_method_id = Column(Integer, autoincrement=True, primary_key=True)
    call_method_code = Column(String(10), nullable=False, unique=True)
    call_method_description = Column(String(50), nullable=False)
