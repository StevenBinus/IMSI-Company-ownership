from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCashManagementInType(Base):
    __tablename__ = 'mtr_cash_management_in_type'
    is_active = Column(Boolean, default=True, nullable=False)
    cash_management_in_type_id = Column(Integer, autoincrement=True, primary_key=True)
    cash_management_in_type_code = Column(String(10), nullable=False, unique=True)
    cash_management_in_type_description = Column(String(50), nullable=False)
