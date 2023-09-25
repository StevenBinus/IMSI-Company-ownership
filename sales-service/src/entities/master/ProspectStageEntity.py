from src.configs.database import Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

class MtrProspectStage(Base):
    __tablename__ = "mtr_prospect_stage"
    is_active = Column(Boolean,nullable=False,default=True)
    prospect_stage_id = Column(Integer,primary_key=True,autoincrement=True)
    prospect_stage_code = Column(String(4),unique=True,nullable=False)
    prospect_stage_description = Column(String(10),nullable=True,default="")
    #back populates
    prospectstage_prospectheader = relationship("TrxProspectHeader",back_populates="prospectheader_prospectstage",foreign_keys="TrxProspectHeader.prospect_stage_id")