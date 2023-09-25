from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrApprovalDiscount(Base):
    __tablename__ = 'mtr_approval_discount'
    is_active = Column(Boolean, default=True, nullable=False)
    approval_discount_id = Column(Integer, autoincrement=True, primary_key=True)
    approval_discount = Column(String(20), nullable=False, unique=True)
    approval_discount_description = Column(String(256), nullable=False)