from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBankType(Base):
    __tablename__ = 'mtr_bank_type'
    is_active = Column(Boolean, default=True, nullable=False)
    bank_type_id = Column(Integer, autoincrement=True, primary_key=True)
    bank_type_code = Column(String(25), nullable=False, unique=True)
    bank_type_description = Column(String(50), nullable=False)