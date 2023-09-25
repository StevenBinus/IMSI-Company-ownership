from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTransferOutStatus(Base):
    __tablename__ = 'mtr_transfer_out_status'
    is_active = Column(Boolean, default=True, nullable=False)
    transfer_out_status_id = Column(Integer, autoincrement=True, primary_key=True)
    transfer_out_status_code = Column(String(20),nullable=False, unique=True)
    transfer_out_status_description = Column(String(256), nullable=False)