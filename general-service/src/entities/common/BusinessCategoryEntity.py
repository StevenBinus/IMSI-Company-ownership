from sqlalchemy import Column, Boolean, String, Integer
from src.configs.database import Base
from sqlalchemy.orm import relationship


class MtrBusinessCategory(Base):
    __tablename__ = "mtr_business_category"
    is_active = Column(Boolean, nullable=False, default=True)
    business_category_id = Column(Integer, primary_key=True, autoincrement=True)
    business_category_code = Column(String(20), nullable=False, unique=True)
    business_category_name = Column(String(256), nullable=True, default="")

    # back populates
    company_business_category = relationship("MtrCompany",back_populates="business_category_company",foreign_keys="MtrCompany.business_category_id")
    profit_center_business_category = relationship(
        "MtrProfitCenter",
        back_populates="business_category_profit_center",
        foreign_keys="MtrProfitCenter.business_category_id",
    )
