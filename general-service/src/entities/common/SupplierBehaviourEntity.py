from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrSupplierBehaviour(Base):
    __tablename__ = 'mtr_supplier_behaviour'
    is_active = Column(Boolean, default=True, nullable=False)
    supplier_behaviour_id = Column(Integer, autoincrement=True, primary_key=True)
    supplier_behaviour_code = Column(String(20),nullable=False, unique=True)
    supplier_behaviour_description = Column(String(256), nullable=False)

    #back populates
    behaviour_supplier = relationship("MtrSupplier", back_populates="supplier_behaviour", foreign_keys="MtrSupplier.supplier_behaviour_id")
    customer_behavior_bfk = relationship("MtrCustomer", back_populates="customer_behavior_fk", foreign_keys="MtrCustomer.customer_behavior_id")