from sqlalchemy import Column,String,Integer,Float,Identity
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrDealerRepresentative(Base):
    __tablename__ = "mtr_dealer_representative"
    dealer_representative_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    dealer_representative_code = Column(Float, nullable=False)
    dealer_representative_name = Column(String(128), nullable=True, default="")
    dealer_representative_cost_center_sequence = Column(Float, nullable=True, default=0)

    #back populates
    dealer_representative_bfk = relationship("MtrCostProfitMap", back_populates="dealer_representative_fk", foreign_keys="MtrCostProfitMap.dealer_representative_id")



