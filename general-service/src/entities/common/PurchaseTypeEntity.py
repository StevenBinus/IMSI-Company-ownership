from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrPurchaseType(Base):
    __tablename__ = 'mtr_purchase_type'
    is_active = Column(Boolean, default=True, nullable=False)
    purchase_type_id = Column(Integer, autoincrement=True, primary_key=True)
    purchase_type_code = Column(String(20),nullable=False, unique=True)
    purchase_type_description = Column(String(256), nullable=False)