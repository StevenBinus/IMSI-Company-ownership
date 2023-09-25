from sqlalchemy import String,Column,Integer, Boolean
from sqlalchemy.orm import relationship 
from src.configs.database import Base

class MtrGender(Base):
    __tablename__ = 'mtr_gender'
    is_active = Column(Boolean, default=True, nullable=False)
    gender_id = Column(Integer, autoincrement=True, primary_key=True)
    gender_code = Column(String(10), nullable=False, unique=True)
    gender_description = Column(String(50), nullable=False)

    #back populates
    customer_gender_bfk = relationship("MtrCustomer", back_populates="customer_gender_fk", foreign_keys="MtrCustomer.customer_gender_id")