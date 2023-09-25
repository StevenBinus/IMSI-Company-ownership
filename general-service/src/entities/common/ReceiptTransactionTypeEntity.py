from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrReceiptTransactionType(Base):
    __tablename__ = 'mtr_receipt_transaction_type'
    is_active = Column(Boolean, default=True, nullable=False)
    receipt_transaction_type_id = Column(Integer, autoincrement=True, primary_key=True)
    receipt_transaction_type_code = Column(String(5),nullable=False, unique=True)
    receipt_transaction_type_description = Column(String(10), nullable=False)