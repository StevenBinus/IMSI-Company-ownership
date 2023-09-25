from sqlalchemy import String, Column, Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship


class MtrBusinessScope(Base):
    __tablename__ = "mtr_business_scope"
    is_active = Column(Boolean, default=True, nullable=False)
    business_scope_id = Column(Integer, autoincrement=True, primary_key=True)
    business_scope_code = Column(String(20), nullable=False, unique=True)
    business_scope_name = Column(String(256), nullable=False)

    # back populates
    company_business_scope = relationship("MtrCompany",back_populates="business_scope_company",foreign_keys="MtrCompany.business_scope_id")
