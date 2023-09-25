from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrRFPPaidIn(Base):
    __tablename__ = 'mtr_rfp_paid_in'
    is_active = Column(Boolean, default=True, nullable=False)
    rfp_paid_in_id = Column(Integer, autoincrement=True, primary_key=True)
    rfp_paid_in_code = Column(String(5),nullable=False, unique=True)
    rfp_paid_in_description = Column(String(50), nullable=False)