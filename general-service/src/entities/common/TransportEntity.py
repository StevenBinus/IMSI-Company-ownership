from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTransport(Base):
    __tablename__ = 'mtr_transport'
    is_active = Column(Boolean, default=True, nullable=False)
    transport_id = Column(Integer, autoincrement=True, primary_key=True)
    transport_code = Column(String(25),nullable=False, unique=True)
    transport_description = Column(String(50), nullable=False)