from sqlalchemy import Column, Integer, Boolean, String
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrAfterSalesArea(Base):
    __tablename__ = "mtr_aftersales_area"
    is_active = Column(Boolean, nullable=False, default=True)
    after_sales_area_id = Column(Integer, autoincrement=True, primary_key=True)
    after_sales_area_code = Column(String(20), nullable=False, unique=True)
    after_sales_area_name = Column(String(256), nullable=True, default="")

    # back populates
    company_aftersales_area = relationship("MtrCompany",back_populates="aftersales_area_company",foreign_keys="MtrCompany.aftersales_area_id")
