from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTransactionTypePPh(Base):
    __tablename__ = 'mtr_transaction_type_pph'
    is_active = Column(Boolean, default=True, nullable=False)
    transaction_type_pph_id = Column(Integer, autoincrement=True, primary_key=True)
    transaction_type_pph_code = Column(String(20),nullable=False, unique=True)
    transaction_type_pph_description = Column(String(256), nullable=False)