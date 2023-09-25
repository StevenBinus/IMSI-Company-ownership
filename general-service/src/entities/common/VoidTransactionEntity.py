from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrVoidTransaction(Base):
    __tablename__ = 'mtr_void_transaction'
    is_active = Column(Boolean, default=True, nullable=False)
    void_transaction_id = Column(Integer, autoincrement=True, primary_key=True)
    void_transaction_code = Column(String(20), nullable=False, unique=True)
    void_transaction_name = Column(String(256), nullable=False,)