from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrWorkOrderSiteType(Base):
    __tablename__ = 'mtr_work_order_site_type'
    is_active = Column(Boolean, default=True, nullable=False)
    work_order_site_type_id = Column(Integer, autoincrement=True, primary_key=True)
    work_order_site_type_code = Column(String(20),nullable=False, unique=True)
    work_order_site_type_description = Column(String(256), nullable=False)