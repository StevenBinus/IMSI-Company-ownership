from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrApprovalSpm(Base):
    __tablename__ = 'mtr_approval_spm'
    is_active = Column(Boolean, default=True, nullable=False)
    approval_spm_id = Column(Integer, autoincrement=True, primary_key=True)
    approval_spm_code = Column(String(20), nullable=False, unique=True)
    approval_spm_name = Column(String(256), nullable=False)

    #back populates
    comref_appspm=relationship("MtrCompanyReference",back_populates="appspm_comref",foreign_keys="MtrCompanyReference.approval_spm_id")