from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrDeliveryMethod(Base):
    __tablename__ = 'mtr_delivery_method'
    is_active = Column(Boolean, default=True, nullable=False)
    delivery_method_id = Column(Integer, autoincrement=True, primary_key=True)
    delivery_method_code = Column(String(10), nullable=False, unique=True)
    delivery_method_description = Column(String(50), nullable=False)