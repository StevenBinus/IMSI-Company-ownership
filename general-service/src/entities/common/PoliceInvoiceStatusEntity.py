from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrPoliceInvoiceStatus(Base):
    __tablename__ = 'mtr_police_invoice_status'
    is_active = Column(Boolean, default=True, nullable=False)
    police_invoice_status_id = Column(Integer, autoincrement=True, primary_key=True)
    police_invoice_status_code = Column(String(20),nullable=False, unique=True)
    police_invoice_status_description = Column(String(256), nullable=False)