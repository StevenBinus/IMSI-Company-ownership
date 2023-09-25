from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrPaymentMethodCredit(Base):
    __tablename__ = 'mtr_payment_method_credit'
    is_active = Column(Boolean, default=True, nullable=False)
    payment_method_credit_id = Column(Integer, autoincrement=True, primary_key=True)
    payment_method_credit_code = Column(String(5), nullable=False, unique=True)
    payment_method_credit_name = Column(String(100), nullable=False)