from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCashManagementOutType(Base):
    __tablename__ = 'mtr_cash_management_out_type'
    is_active = Column(Boolean, default=True, nullable=False)
    cash_management_out_type_id = Column(Integer, autoincrement=True, primary_key=True)
    cash_management_out_type_code = Column(String(10), nullable=False, unique=True)
    cash_management_out_type_description = Column(String(50), nullable=False)
