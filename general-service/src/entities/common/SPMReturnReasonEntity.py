from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrSPMReturnReason(Base):
    __tablename__ = 'mtr_spm_return_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    spm_return_reason_id = Column(Integer, autoincrement=True, primary_key=True)
    spm_return_reason_code = Column(String(20),nullable=False, unique=True)
    spm_return_reason_description = Column(String(256), nullable=False)