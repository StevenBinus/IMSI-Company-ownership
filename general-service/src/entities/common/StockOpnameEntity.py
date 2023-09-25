from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrStockOpname(Base):
    __tablename__ = 'mtr_stock_opname'
    is_active = Column(Boolean, default=True, nullable=False)
    stock_opname_id = Column(Integer, autoincrement=True, primary_key=True)
    stock_opname_code = Column(String(20),nullable=False, unique=True)
    stock_opname_description = Column(String(256), nullable=False)