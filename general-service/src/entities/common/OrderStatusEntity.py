from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrOrderStatus(Base):
    __tablename__ = 'mtr_order_status'
    is_active = Column(Boolean, default=True, nullable=False)
    order_status_id = Column(Integer, autoincrement=True, primary_key=True)
    order_status_code = Column(String(25), nullable=False, unique=True)
    order_status_name = Column(String(50), nullable=False)