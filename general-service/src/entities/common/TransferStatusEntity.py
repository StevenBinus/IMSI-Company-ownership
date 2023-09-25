from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTransferStatus(Base):
    __tablename__ = 'mtr_transfer_status'
    is_active = Column(Boolean, default=True, nullable=False)
    transfer_status_id = Column(Integer, autoincrement=True, primary_key=True)
    transfer_status_code = Column(String(50),nullable=False, unique=True)
    transfer_status_description = Column(String(50), nullable=False)