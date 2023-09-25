from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrRequestForPaymentReferenceType(Base):
    __tablename__ = 'mtr_request_for_payment_reference_type'
    is_active = Column(Boolean, default=True, nullable=False)
    request_for_payment_reference_type_id = Column(Integer, autoincrement=True, primary_key=True)
    request_for_payment_reference_type_code = Column(String(5),nullable=False, unique=True)
    request_for_payment_reference_type_description = Column(String(50), nullable=False)