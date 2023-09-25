from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrPaymentMethodCash(Base):
    __tablename__ = 'mtr_payment_method_cash'
    is_active = Column(Boolean, default=True, nullable=False)
    payment_method_cash_id = Column(Integer, autoincrement=True, primary_key=True)
    payment_method_cash_code = Column(String(5), nullable=False, unique=True)
    payment_method_cash_name = Column(String(100), nullable=False)