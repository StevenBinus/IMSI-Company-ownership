from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBillableTo(Base):
    __tablename__ = 'mtr_bill_able_to'
    is_active = Column(Boolean, default=True, nullable=False)
    billable_to_id = Column(Integer, autoincrement=True, primary_key=True)
    billable_to_code = Column(String(10), nullable=False, unique=True)
    billable_to_name = Column(String(50), nullable=False)
