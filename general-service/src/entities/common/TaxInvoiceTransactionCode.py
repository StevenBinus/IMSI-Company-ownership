from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTaxInvoiceTransactionCode(Base):
    __tablename__ = 'mtr_tax_invoce_transaction_code'
    is_active = Column(Boolean, default=True, nullable=False)
    tax_invoce_transaction_code_id = Column(Integer, autoincrement=True, primary_key=True)
    tax_invoce_transaction_code_code = Column(String(20),nullable=False, unique=True)
    tax_invoce_transaction_code_description = Column(String(256), nullable=False)