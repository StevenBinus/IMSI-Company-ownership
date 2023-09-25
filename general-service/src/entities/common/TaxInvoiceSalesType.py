from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTaxInvoiceSalesType(Base):
    __tablename__ = 'mtr_tax_invoce_sales_type'
    is_active = Column(Boolean, default=True, nullable=False)
    tax_invoce_sales_type_id = Column(Integer, autoincrement=True, primary_key=True)
    tax_invoce_type_sales_code = Column(String(20),nullable=False, unique=True)
    tax_invoce_type_sales_description = Column(String(256), nullable=False)