from sqlalchemy import Column, Identity,Integer,Boolean,String
from sqlalchemy.orm import relationship 
from src.configs.database import Base

class MtrTaxInvoiceType(Base):
    __tablename__ = 'mtr_tax_invoice_type'
    is_active = Column(Boolean, default=True, nullable=False)
    tax_invoice_type_id = Column(Integer, autoincrement=True, primary_key=True)
    tax_invoice_type_code = Column(String(20),nullable=False, unique=True)
    tax_invoice_type_description = Column(String(256), nullable=False)

    tax_customer = relationship("MtrCustomer", back_populates="customer_tax", foreign_keys="MtrCustomer.tax_invoice_type_id")