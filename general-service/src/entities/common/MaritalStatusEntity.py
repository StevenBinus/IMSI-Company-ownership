from sqlalchemy import String,Column,Integer, Boolean
from sqlalchemy.orm import relationship 
from src.configs.database import Base

class MtrMaritalStatus(Base):
    __tablename__ = 'mtr_marital_status'
    is_active = Column(Boolean, default=True, nullable=False)
    marital_status_id = Column(Integer, autoincrement=True, primary_key=True)
    marital_status_code = Column(String(25), nullable=False, unique=True)
    marital_status_description = Column(String(50), nullable=False)

    #back populates
    customer_marital_status_bfk = relationship("MtrCustomer", back_populates="customer_marital_status_fk", foreign_keys="MtrCustomer.customer_marital_status_id")