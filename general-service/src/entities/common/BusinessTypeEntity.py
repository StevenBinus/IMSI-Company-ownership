from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrBusinessType(Base):
    __tablename__ = 'mtr_business_type'
    is_active = Column(Boolean, default=True, nullable=False)
    business_type_id = Column(Integer, autoincrement=True, primary_key=True)
    business_type_code = Column(String(20), nullable=False, unique=True)
    business_type_name = Column(String(256), nullable=False)

    #back populates
    customer_business_type_id_bfk = relationship("MtrCustomer", back_populates="business_type_id_fk", foreign_keys="MtrCustomer.business_type_id")

