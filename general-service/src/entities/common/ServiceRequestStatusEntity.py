from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrServiceRequestReferenceStatus(Base):
    __tablename__ = 'mtr_service_request_reference_status'
    is_active = Column(Boolean, default=True, nullable=False)
    service_request_reference_status_id = Column(Integer, autoincrement=True, primary_key=True)
    service_request_reference_status_code = Column(String(20),nullable=False, unique=True)
    service_request_reference_status_description = Column(String(256), nullable=False)