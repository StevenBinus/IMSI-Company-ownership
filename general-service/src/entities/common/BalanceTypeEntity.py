from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBalanceType(Base):
    __tablename__ = 'mtr_balance_type'
    is_active = Column(Boolean, default=True, nullable=False)
    balance_type_id = Column(Integer, autoincrement=True, primary_key=True)
    balance_type_code = Column(String(20), nullable=False, unique=True)
    balance_type_description = Column(String(256), nullable=False)