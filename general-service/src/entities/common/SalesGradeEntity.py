from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSalesGrade(Base):
    __tablename__ = 'mtr_sales_grade'
    is_active = Column(Boolean, default=True, nullable=False)
    sales_grade_id = Column(Integer, autoincrement=True, primary_key=True)
    sales_grade_code = Column(String(10),nullable=False, unique=True)
    sales_grade_name = Column(String(50),nullable=False)