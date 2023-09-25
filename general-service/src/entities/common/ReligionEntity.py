from sqlalchemy import String,Column,Integer, Boolean
from sqlalchemy.orm import relationship 
from src.configs.database import Base

class MtrReligion(Base):
    __tablename__ = 'mtr_religion'
    is_active = Column(Boolean, default=True, nullable=False)
    religion_id = Column(Integer, autoincrement=True, primary_key=True)
    religion_code = Column(String(25), nullable=False, unique=True)
    religion_description = Column(String(50), nullable=False)

    #back populates
    customer_religion_bfk = relationship("MtrCustomer", back_populates="customer_religion_fk", foreign_keys="MtrCustomer.customer_religion_id")