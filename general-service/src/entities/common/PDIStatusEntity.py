from sqlalchemy import Column, Identity,Integer,Boolean,String
from src.configs.database import Base

class MtrPDIStatus(Base):
    __tablename__ = 'mtr_pdi_status'
    is_active = Column(Boolean, default=True, nullable=False)
    pdi_status_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    pdi_status_code = Column(String(25),nullable=False, unique=True)
    pdi_status_description = Column(String(50), nullable=False)