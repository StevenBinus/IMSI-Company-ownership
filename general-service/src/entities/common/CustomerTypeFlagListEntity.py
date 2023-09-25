from sqlalchemy import CHAR,String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrCustomerTypeFlagList(Base):
    __tablename__ = 'mtr_customer_type_flag_list'
    is_active = Column(Boolean, default=True, nullable=False)
    customer_type_flag_list_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_type_flag_list_code = Column(CHAR(1), nullable=False, unique=True)
    customer_type_flag_list_name = Column(String(20), nullable=False)

    #back populates
    customer_type_bfk = relationship("MtrCustomerType", back_populates="customer_type_flag_list_fk", foreign_keys="MtrCustomerType.customer_type_flag_list_id")
