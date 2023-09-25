from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrPurchaseReturnReason(Base):
    __tablename__ = 'mtr_purchase_return_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    purchase_return_reason_id = Column(Integer, autoincrement=True, primary_key=True)
    purchase_return_reason_code = Column(String(20),nullable=False, unique=True)
    purchase_return_reason_description = Column(String(256), nullable=False)