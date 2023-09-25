from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTransactionTypeCashManagementDP(Base):
    __tablename__ = 'mtr_transaction_type_cash_management_dp'
    is_active = Column(Boolean, default=True, nullable=False)
    transaction_type_cash_management_dp_id = Column(Integer, autoincrement=True, primary_key=True)
    transaction_type_cash_management_dp_code = Column(String(20),nullable=False, unique=True)
    transaction_type_cash_management_dp_description = Column(String(256), nullable=False)