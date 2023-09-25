from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCashFlowType(Base):
    __tablename__ = 'mtr_cash_flow_type'
    is_active = Column(Boolean, default=True, nullable=False)
    cash_flow_type_id = Column(Integer, autoincrement=True, primary_key=True)
    cash_flow_type_code = Column(String(10), nullable=False, unique=True)
    cash_flow_type_description = Column(String(50), nullable=False)
