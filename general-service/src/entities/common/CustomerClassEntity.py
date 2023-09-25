from sqlalchemy import CHAR,String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrCustomerClass(Base):
    __tablename__ = 'mtr_customer_class'
    is_active = Column(Boolean, default=True, nullable=False)
    customer_class_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_class_code = Column(CHAR(3), nullable=False, unique=True)
    customer_class_name = Column(String(20))

    #back populates
    customer_class_bfk = relationship("MtrCustomer", back_populates="customer_class_fk", foreign_keys="MtrCustomer.customer_class_id")
    customer_class_supplier = relationship("MtrSupplier", back_populates="supplier_customer_class", foreign_keys="MtrSupplier.supplier_class_id")