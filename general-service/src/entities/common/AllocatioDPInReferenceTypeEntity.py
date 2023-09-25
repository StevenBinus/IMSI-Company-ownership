from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrAllocationDPInReferenceType(Base):
    __tablename__ = 'mtr_allocation_dp_in_reference_type'
    is_active = Column(Boolean, default=True, nullable=False)
    allocation_dp_in_reference_type_id = Column(Integer, autoincrement=True, primary_key=True)
    allocation_dp_in_reference_type_code = Column(String(20),nullable=False, unique=True)
    allocation_dp_in_reference_type_description = Column(String(256), nullable=False)