from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrSupplierCustomerGroup(Base):
    __tablename__ = 'mtr_supplier_customer_group'
    is_active = Column(Boolean, default=True, nullable=False)
    supplier_customer_group_id = Column(Integer, autoincrement=True, primary_key=True)
    supplier_customer_group_code = Column(String(20),nullable=False, unique=True)
    supplier_customer_group_description = Column(String(256), nullable=False)

    #back populates
    mtr_customer_type_bfk = relationship("MtrCustomerType", back_populates="supplier_customer_group_fk", foreign_keys="MtrCustomerType.supplier_customer_group_id")
    supplier_customer_type = relationship("MtrSupplierType",back_populates="supplier_type_customer",foreign_keys="MtrSupplierType.supplier_group_id")
