from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSalesCategory(Base):
    __tablename__ = 'mtr_sales_category'
    is_active = Column(Boolean, default=True, nullable=False)
    sales_category_id = Column(Integer, autoincrement=True, primary_key=True)
    sales_category_code = Column(String(20),nullable=False, unique=True)
    sales_category_description = Column(String(256), nullable=False)