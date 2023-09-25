from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrShippingMethod(Base):
    __tablename__ = 'mtr_shipping_method'
    is_active = Column(Boolean, default=True, nullable=False)
    shipping_method_id = Column(Integer, autoincrement=True, primary_key=True)
    shipping_method_code = Column(String(20),nullable=False, unique=True)
    shipping_method_description = Column(String(256), nullable=False)