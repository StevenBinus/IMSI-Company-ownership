from src.configs.database import Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

class MtrFollowUp(Base):
    __tablename__ = "mtr_follow_up"
    is_active = Column(Boolean,nullable=False,default=True)
    follow_up_id = Column(Integer,primary_key=True,autoincrement=True)
    follow_up_code = Column(String(4),unique=True,nullable=False)
    follow_up_description = Column(String(128),nullable=True,default="")
    #back populates
    follow_followup = relationship("TrxProspectFollowUp",back_populates="followup_follow",foreign_keys="TrxProspectFollowUp.follow_up_id")