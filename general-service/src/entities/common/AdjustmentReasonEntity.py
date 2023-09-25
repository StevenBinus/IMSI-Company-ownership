from sqlalchemy import Column,Integer,Boolean,String
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrAdjustmentReason(Base):
    __tablename__ = 'mtr_adjustment_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    adjustment_reason_id = Column(Integer, autoincrement=True, primary_key=True)
    adjustment_reason_code = Column(String(20),nullable=False, unique=True)
    adjustment_reason_name = Column(String(256), nullable=False)

    #back populates
    comref_adjustment=relationship("MtrCompanyReference",back_populates="adjustment_comref",foreign_keys="MtrCompanyReference.adjustment_reason_id")