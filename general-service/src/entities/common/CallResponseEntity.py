from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCallResponse(Base):
    __tablename__ = 'mtr_call_response'
    is_active = Column(Boolean, default=True, nullable=False)
    call_response_id = Column(Integer, autoincrement=True, primary_key=True)
    call_response_code = Column(String(10), nullable=False, unique=True)
    call_response_description = Column(String(50), nullable=False)
