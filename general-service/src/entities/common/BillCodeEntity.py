from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBillCode(Base):
    __tablename__ = 'mtr_bill_code'
    is_active = Column(Boolean, default=True, nullable=False)
    bill_code_id = Column(Integer, autoincrement=True, primary_key=True)
    bill_code = Column(String(10), nullable=False, unique=True)
    bill_code_description = Column(String(50), nullable=False)
