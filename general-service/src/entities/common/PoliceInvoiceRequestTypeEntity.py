from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrPoliceInvoiceRequestType(Base):
    __tablename__ = 'mtr_police_invoice_request'
    is_active = Column(Boolean, default=True, nullable=False)
    police_invoice_request_type_id = Column(Integer, autoincrement=True, primary_key=True)
    police_invoice_request_type_code = Column(String(20),nullable=False, unique=True)
    police_invoice_request_type_description = Column(String(256), nullable=False)