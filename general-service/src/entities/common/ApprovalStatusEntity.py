from sqlalchemy import String,Column,Integer, Boolean
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrApprovalStatus(Base):
    __tablename__ = 'mtr_approval_status'
    is_active = Column(Boolean, default=True, nullable=False)
    approval_status_id = Column(Integer, autoincrement=True, primary_key=True)
    approval_status_code = Column(Integer, nullable=False, unique=True)
    approval_status_description = Column(String(20), nullable=False)

    #back populates
    approval_bfk = relationship("MtrCustomerVirtualAccount", back_populates="approval_fk", foreign_keys="MtrCustomerVirtualAccount.approval_dbs")