from sqlalchemy import Column,String,Integer,Identity,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCostProfitMap(Base):
    __tablename__ = "mtr_cost_profit_map"
    is_acitve = Column(Boolean, default=True, nullable=False)
    company_id = Column(Integer, ForeignKey("mtr_company.company_id"), nullable=False)
    cost_profit_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    profit_center_id = Column(Integer, ForeignKey("mtr_profit_center.profit_center_id"), nullable=False)
    cost_center_id = Column(Integer, ForeignKey("mtr_cost_center.cost_center_id"), nullable=False)
    mapping_description = Column(String(100), nullable=True, default="")
    city_id = Column(Integer, ForeignKey("mtr_city.city_id"), nullable=True)
    dealer_representative_id = Column(Integer, ForeignKey("mtr_dealer_representative.dealer_representative_id"), nullable=True)

    # back populates
    company_cost_fk = relationship("MtrCompany", back_populates="company_cost_bfk", foreign_keys=[company_id])
    profit_center_fk = relationship("MtrProfitCenter", back_populates="profit_center_bfk", foreign_keys=[profit_center_id])
    cost_center_fk = relationship("MtrCostCenter", back_populates="cost_center_bfk", foreign_keys=[cost_center_id])
    city_fk = relationship("MtrCity", back_populates="city_bfk", foreign_keys=[city_id])
    dealer_representative_fk = relationship("MtrDealerRepresentative", back_populates="dealer_representative_bfk", foreign_keys=[dealer_representative_id])



