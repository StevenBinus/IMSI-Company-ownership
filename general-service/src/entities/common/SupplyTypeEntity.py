from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSupplyType(Base):
    __tablename__ = 'mtr_supply_type'
    is_active = Column(Boolean, default=True, nullable=False)
    supply_type_id = Column(Integer, autoincrement=True, primary_key=True)
    supply_type_code = Column(String(20),nullable=False, unique=True)
    supply_type_description = Column(String(256), nullable=False)