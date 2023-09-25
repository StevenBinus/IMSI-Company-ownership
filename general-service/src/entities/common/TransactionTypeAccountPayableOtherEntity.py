from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTransactionTypeAccountPayableOther(Base):
    __tablename__ = 'mtr_transaction_type_account_payable_other'
    is_active = Column(Boolean, default=True, nullable=False)
    transaction_type_account_payable_other_id = Column(Integer, autoincrement=True, primary_key=True)
    transaction_type_account_payable_other_code = Column(String(5),nullable=False, unique=True)
    transaction_type_account_payable_other_description = Column(String(100), nullable=False)