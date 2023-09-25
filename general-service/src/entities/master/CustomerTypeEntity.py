from sqlalchemy import Column, String, Integer, CHAR, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerType(Base):
    __tablename__ = "mtr_customer_type"
    is_active = Column(Boolean, nullable=False, default=True)
    customer_type_id = Column(Integer, autoincrement=True,primary_key=True)
    customer_type = Column(CHAR(2), nullable=False, default="")
    customer_type_description = Column(String(35), nullable=False, default="")
    customer_type_flag_list_id = Column(Integer, ForeignKey("mtr_customer_type_flag_list.customer_type_flag_list_id"))
    supplier_customer_group_id = Column(Integer, ForeignKey("mtr_supplier_customer_group.supplier_customer_group_id"))
    vehicle_sales_order = Column(Boolean, nullable=False, default=True)
    bbn = Column(Boolean, nullable=False, default=True)
    police_invoice = Column(Boolean, nullable=False, default=True)
    tax_free = Column(Boolean, nullable=False, default=True)

    #back populates
    customer_type_flag_list_fk = relationship("MtrCustomerTypeFlagList", back_populates="customer_type_bfk", foreign_keys=[customer_type_flag_list_id])
    supplier_customer_group_fk = relationship("MtrSupplierCustomerGroup", back_populates="mtr_customer_type_bfk", foreign_keys=[supplier_customer_group_id])

    customer_bfk = relationship("MtrCustomer", back_populates="customer_type_fk", foreign_keys="MtrCustomer.customer_type_id")
