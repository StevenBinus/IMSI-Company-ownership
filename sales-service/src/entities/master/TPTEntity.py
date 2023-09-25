from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrTPT(Base):
    __tablename__ = "mtr_tpt"
    is_active = Column(Boolean,nullable=False, default=True)
    tpt_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    tpt_type = Column(CHAR(1),nullable=False)
    tpt_quota = Column(Integer,nullable=False)
    tpt_remaining = Column(Integer,nullable=False)
    tpt_used = Column(Integer,nullable=False)
    tpt_status = Column(CHAR(1),nullable=False)
    unit_variant_id = Column(Integer,ForeignKey("mtr_unit_variant.variant_id"))
    #back populates
    tpt_tptchassis = relationship("MtrTPTChassis", back_populates="tptchassis_tpt", foreign_keys="MtrTPTChassis.tpt_id")