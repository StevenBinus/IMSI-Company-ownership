from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrFundType(Base):
    __tablename__ = 'mtr_fund_type'
    is_active = Column(Boolean, default=True, nullable=False)
    fund_type_id = Column(Integer, autoincrement=True, primary_key=True)
    fund_type_code = Column(String(10), nullable=False, unique=True)
    fund_type_description = Column(String(50), nullable=False)