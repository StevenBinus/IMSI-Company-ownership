from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrProspectSource(Base):
    __tablename__ = "mtr_prospect_source"
    is_active = Column(Boolean, nullable=False, default=True)
    prospect_source_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True
    )
    prospect_group_id = Column(Integer, nullable=False)
    # prospect_group_id = Column(Integer,ForeignKey("mtr_prospect_group"),nullable=False)
    company_id = Column(Integer, nullable=False)
    # company_id = Column(Integer,ForeignKey("mtr_company.company_id"),nullable=False)
    prospect_source_code = Column(String(10), nullable=False, default="")
    prospect_source_name = Column(String(50), nullable=True, default="")

    # mvc_prospect_group = relationship("MtrProspectGroup",back_populates="prospect_group_mvc",foreign_keys=[prospect_group_id])
    # company_prospectsource = relationship(
    #     "MtrCompany",
    #     back_populates="prospectsource_company",
    #     foreign_keys=[company_id],
    # )
