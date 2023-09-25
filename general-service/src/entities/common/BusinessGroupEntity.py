from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrBusinessGroup(Base):
    __tablename__ = 'mtr_business_group'
    is_active = Column(Boolean, default=True, nullable=False)
    business_group_id = Column(Integer, autoincrement=True, primary_key=True)
    business_group_code = Column(String(10), nullable=False, unique=True)
    business_group_name = Column(String(50), nullable=False)

    #back populates
    customer_business_group_id_bfk = relationship("MtrCustomer", back_populates="business_group_id_fk", foreign_keys="MtrCustomer.business_group_id")
    reference_business_group=relationship("MtrSupplierReferenceEntity",back_populates="business_group_reference",foreign_keys="MtrSupplierReferenceEntity.business_group_id")
