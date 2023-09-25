from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSPMReturnStatus(Base):
    __tablename__ = 'mtr_spm_return_status'
    is_active = Column(Boolean, default=True, nullable=False)
    spm_return_status_id = Column(Integer, autoincrement=True, primary_key=True)
    spm_return_status_code = Column(String(20),nullable=False, unique=True)
    spm_return_status_description = Column(String(256), nullable=False)