from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrAccountPayableInvoiceType(Base):
    __tablename__ = 'mtr_account_payable_invoice_type'
    is_active = Column(Boolean, default=True, nullable=False)
    account_payable_invoice_type_id = Column(Integer, autoincrement=True, primary_key=True)
    account_payable_invoice_type_code = Column(String(20),nullable=False, unique=True)
    account_payable_invoice_type_description = Column(String(256), nullable=False)