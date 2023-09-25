from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrStockOpnameStatus(Base):
    __tablename__ = 'mtr_stock_opname_status'
    is_active = Column(Boolean, default=True, nullable=False)
    stock_opname_status_id = Column(Integer, autoincrement=True, primary_key=True)
    stock_opname_status_code = Column(String(25), primary_key=True)
    stock_opname_status_name = Column(String(100), nullable=False)