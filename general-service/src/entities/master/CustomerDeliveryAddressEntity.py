from sqlalchemy import Column, String, Integer, CHAR, Boolean,ForeignKey,Identity, UniqueConstraint
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerDeliveryAddress(Base):
    __tablename__ = "mtr_customer_delivery_address"
    
    customer_delivery_address_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, default=True)
    customer_id = Column(Integer, ForeignKey("mtr_customer.customer_id"), nullable=False)
    ship_to_line_number = Column(Integer, nullable=False)
    ship_to_name = Column(String(100), nullable=False)
    address_id = Column(Integer, ForeignKey("mtr_address.address_id"), nullable=True, default=0)
    phone_number = Column(String(30), nullable=True)
    fax_number = Column(String(30), nullable=True)
    lead_times = Column(Integer, nullable=True)
    contact_person = Column(String(100), nullable=True, default="")
    job_title_id = Column(Integer, ForeignKey("mtr_job_title.job_title_id"), nullable=True, default=0)


    __table_args__ = (UniqueConstraint('customer_id', 'ship_to_line_number', name='_unique_field_customer_ship'),)
    customer_delivery_fk = relationship("MtrCustomer", back_populates="customer_delivery_bfk",foreign_keys=[customer_id])
    address_delivery_fk = relationship("MtrAddress", back_populates="address_delivery_bfk",foreign_keys=[address_id])
    Jobtitle_fk = relationship("MtrJobTitle", back_populates="Jobtitle_bfk",foreign_keys=[job_title_id])