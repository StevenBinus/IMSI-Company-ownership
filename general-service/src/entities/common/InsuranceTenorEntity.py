from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrInsuranceTenor(Base):
    __tablename__ = 'mtr_insurance_tenor'
    is_active = Column(Boolean, default=True, nullable=False)
    insurance_tenor_id = Column(Integer, autoincrement=True, primary_key=True)
    insurance_tenor_code = Column(String(10), nullable=False, unique=True)
    insurance_tenor_description = Column(String(50), nullable=False)