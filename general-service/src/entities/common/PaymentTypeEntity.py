from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrPaymentType(Base):
    __tablename__ = 'mtr_payment_type'
    is_active = Column(Boolean, default=True, nullable=False)
    payment_type_id = Column(Integer, autoincrement=True, primary_key=True)
    payment_type_code = Column(String(5), nullable=False, unique=True)
    payment_type_name = Column(String(100), nullable=False) 