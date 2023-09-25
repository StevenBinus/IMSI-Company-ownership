from src.configs.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey, DateTime
from sqlalchemy.orm import relationship

class TrxProspectFollowUp(Base):
    __tablename__ = "trx_prospect_followup"
    trx_prospect_followup_id = Column(Integer,primary_key=True,autoincrement=True)
    prospect_system_number = Column(Integer,ForeignKey("trx_prospect.prospect_system_number"))
    follow_up_id = Column(Integer,ForeignKey("mtr_follow_up.follow_up_id"))
    prospect_follow_up_date = Column(DateTime,nullable=True,default="")
    prospect_follow_up_note = Column(String(128),nullable=True,default="")
    result_date = Column(DateTime,nullable=True,default="")
    result_note = Column(String(128),nullable=True,default="")
    #back populates
    followup_prospect = relationship("TrxProspectHeader",back_populates="prospect_followup",foreign_keys=[prospect_system_number])
    followup_follow = relationship("MtrFollowUp",back_populates="follow_followup",foreign_keys=[follow_up_id])