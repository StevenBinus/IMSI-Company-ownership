from sqlalchemy import Column, String, Integer, CHAR, Boolean,ForeignKey,Identity,UniqueConstraint
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerContact(Base):
    __tablename__ = "mtr_customer_contact"
    
    customer_contact_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, default=True)
    customer_id = Column(Integer, ForeignKey("mtr_customer.customer_id"), nullable=False)
    contact_line_number = Column(Integer, nullable=False)
    contact_name = Column(String(10), nullable=True, default="")
    description = Column(String(100), nullable=True, default="")
    phone_number = Column(String(30), nullable=True, default="")
    
    __table_args__ = (UniqueConstraint('customer_id', 'contact_line_number', name='_unique_field_customer_contact'),)

    customer_contact_fk = relationship("MtrCustomer", back_populates="customer_contact_bfk",foreign_keys=[customer_id])