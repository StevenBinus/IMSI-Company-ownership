from sqlalchemy import Column,String,Integer,Boolean,ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerByDealer(Base):
    __tablename__ = "mtr_customer_by_dealer"
    customer_by_dealer_id = Column(Integer, autoincrement=True, primary_key=True)
    is_active = Column(Boolean, nullable=False, default=True)
    customer_id = Column(Integer, ForeignKey("mtr_customer.customer_id"), nullable=False)
    company_id = Column(Integer, ForeignKey("mtr_company.company_id"), unique=True, nullable=False)
    
    
    __table_args__ = (UniqueConstraint('customer_id', 'company_id', name='_unique_field_customer_company'),)
    customer_dealer_fk = relationship("MtrCustomer", back_populates="customer_dealer_bfk", foreign_keys=[customer_id])
    company_fk = relationship("MtrCompany", back_populates="company_bfk", foreign_keys=[company_id])