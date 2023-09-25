from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrServiceRequestRefereceType(Base):
    __tablename__ = 'mtr_service_request_reference_type'
    is_active = Column(Boolean, default=True, nullable=False)
    service_request_reference_type_id = Column(Integer, autoincrement=True, primary_key=True)
    service_request_reference_type_code = Column(String(20),nullable=False, unique=True)
    service_request_reference_type_description = Column(String(256), nullable=False)