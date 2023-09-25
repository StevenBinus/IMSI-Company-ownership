from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSupplyReturnReason(Base):
    __tablename__ = 'mtr_supply_return_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    supply_return_reason_id = Column(Integer, autoincrement=True, primary_key=True)
    supply_return_reason_code = Column(String(20),nullable=False, unique=True)
    supply_return_reason_description = Column(String(256), nullable=False)