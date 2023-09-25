from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBillStatus(Base):
    __tablename__ = 'mtr_bill_status'
    is_active = Column(Boolean, default=True, nullable=False)
    bill_status_id = Column(Integer, autoincrement=True, primary_key=True)
    bill_status_code = Column(String(10), nullable=False, unique=True)
    bill_status_description = Column(String(50), nullable=False)
