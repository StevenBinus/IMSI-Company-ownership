from sqlalchemy import Column,Integer,Boolean,String,ForeignKey
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrSupplierType(Base):
    __tablename__ = 'mtr_supplier_type'
    is_active = Column(Boolean, default=True, nullable=False)
    supplier_type_id = Column(Integer, autoincrement=True, primary_key=True)
    supplier_type_code = Column(String(20),nullable=False, unique=True)
    supplier_type_description = Column(String(256), nullable=False)
    supplier_group_id = Column(Integer,ForeignKey("mtr_supplier_customer_group.supplier_customer_group_id"),nullable=False)

    #back populates
    supplier_type_customer = relationship("MtrSupplierCustomerGroup",back_populates="",foreign_keys=[supplier_group_id])
    reference_supplier_type = relationship("MtrSupplierReferenceEntity",back_populates="supplier_type_reference",foreign_keys="MtrSupplierReferenceEntity.supplier_type_id")
