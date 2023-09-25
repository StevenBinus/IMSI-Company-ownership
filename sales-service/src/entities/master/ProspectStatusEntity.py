from sqlalchemy import Column,Integer,Boolean,String
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrProspectStatus(Base):
    __tablename__ = 'mtr_prospect_status'
    is_active = Column(Boolean, default=True, nullable=False)
    prospect_status_id = Column(Integer, autoincrement=True, primary_key=True)
    prospect_status_code = Column(String(20),nullable=False, unique=True)
    prospect_status_description = Column(String(256), nullable=False)
    #back populates
    prospectstatus_prospectheader = relationship("TrxProspectHeader",back_populates="prospectheader_prospectstatus",foreign_keys="TrxProspectHeader.prospect_status_id")