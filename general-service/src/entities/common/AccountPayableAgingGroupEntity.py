from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrAccountPayableAgingGroup(Base):
    __tablename__ = 'mtr_account_payable_aging_group'
    is_active = Column(Boolean, default=True, nullable=False)
    account_payable_aging_group_id = Column(Integer, autoincrement=True, primary_key=True)
    account_payable_aging_group_code = Column(String(20),nullable=False, unique=True)
    account_payable_aging_group_description = Column(String(256), nullable=False)