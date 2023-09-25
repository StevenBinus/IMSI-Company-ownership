from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrUnitPurchaseOrderChangeType(Base):
    __tablename__ = 'mtr_unit_purchase_order_change_type'
    is_active = Column(Boolean, default=True, nullable=False)
    unit_purchase_order_change_type_id = Column(Integer, autoincrement=True, primary_key=True)
    unit_purchase_order_change_type_code = Column(String(20),nullable=False, unique=True)
    unit_purchase_order_change_type_description = Column(String(256), nullable=False)