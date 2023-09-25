from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrPaymentBank(Base):
    __tablename__ = 'mtr_payment_bank'
    is_active = Column(Boolean, default=True, nullable=False)
    payment_bank_id = Column(Integer, autoincrement=True, primary_key=True)
    payment_bank_code = Column(String(5), nullable=False, unique=True)
    payment_bank_name = Column(String(100), nullable=False)