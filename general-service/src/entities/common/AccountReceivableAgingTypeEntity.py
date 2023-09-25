from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrAccountReceivableAgingType(Base):
    __tablename__ = 'mtr_account_receivable_aging_type'
    is_active = Column(Boolean, default=True, nullable=False)
    account_receivable_aging_type_id = Column(Integer, autoincrement=True, primary_key=True)
    account_receivable_aging_type_code = Column(String(20),nullable=False, unique=True)
    account_receivable_aging_type_description = Column(String(256), nullable=False)