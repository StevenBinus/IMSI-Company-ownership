from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrWorkOrderStatus(Base):
    __tablename__ = 'mtr_work_order_status'
    is_active = Column(Boolean, default=True, nullable=False)
    work_order_status_id = Column(Integer, autoincrement=True, primary_key=True)
    work_order_status_code = Column(String(20),nullable=False, unique=True)
    work_order_status_description = Column(String(256), nullable=False)