from sqlalchemy import Column, ForeignKey, String, Boolean, Integer
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerDefaultDelivery(Base):
    __tablename__ = "mtr_customer_default_delivery"
    customer_default_delivery_id = Column(Integer, autoincrement=True, primary_key=True)
    address_id = Column(Integer, ForeignKey("mtr_address.address_id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("mtr_customer.customer_id"), nullable=False, unique=True)
    default_address = Column(Boolean, nullable=True, default=True)
    default_deliver_address_same_with_invoice = Column(Boolean, nullable=True, default=True)
    default_deliver_address = Column(String(100), nullable=True, default="")
    default_deliver_address1 = Column(String(100), nullable=True, default="")
    default_deliver_address2 = Column(String(100), nullable=True, default="")
    default_deliver_contact_person = Column(String(100), nullable=True, default="")
    default_deliver_phone_number = Column(String(100), nullable=True, default="")

    customer_default_delivery = relationship("MtrCustomer", back_populates="default_delivery_customer", foreign_keys=[customer_id])
    address_default_delivery = relationship("MtrAddress", back_populates="default_delivery_address", foreign_keys=[address_id])