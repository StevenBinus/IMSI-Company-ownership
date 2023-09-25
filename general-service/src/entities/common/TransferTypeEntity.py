from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base

class MtrTransferType(Base):
    __tablename__ = 'mtr_transfer_type'
    is_active = Column(Boolean, default=True, nullable=False)
    transfer_type_id = Column(Integer, autoincrement=True, primary_key=True)
    transfer_type_code = Column(String(25),nullable=False, unique=True)
    transfer_type_description = Column(String(50), nullable=False)