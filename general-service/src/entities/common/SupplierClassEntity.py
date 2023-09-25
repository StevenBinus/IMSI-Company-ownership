from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSupplierClass(Base):
    __tablename__ = 'mtr_supplier_class'
    is_active = Column(Boolean, default=True, nullable=False)
    supplier_class_id = Column(Integer, autoincrement=True, primary_key=True)
    supplier_class_code = Column(String(20),nullable=False, unique=True)
    supplier_class_description = Column(String(256), nullable=False)