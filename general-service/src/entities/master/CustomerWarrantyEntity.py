from sqlalchemy import Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerWarranty(Base):
    __tablename__ = "mtr_customer_warranty"
    customer_warranty_id = Column(Integer, autoincrement=True, primary_key=True)
    is_active = Column(Boolean, nullable=False, default=True)
    employee_id = Column(Integer, ForeignKey("mtr_user_details.user_employee_id"),nullable=False)
    customer_id = Column(Integer, ForeignKey("mtr_customer.customer_id"),nullable=False)

    warranty_employee = relationship("MtrUserDetails", back_populates="employee_warranty", foreign_keys=[employee_id])
    warranty_customer = relationship("MtrCustomer", back_populates="customer_warranty", foreign_keys=[customer_id])


