from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrAccessoriesOption(Base):
    __tablename__ = "mtr_accessories_option"
    is_active = Column(Boolean,nullable=False,default=False)
    accessories_option_id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    accessories_option_code = Column(String(15),unique=True,nullable=False)
    accessories_option_name = Column(String(50),nullable=False)
    #back_populates
    accessories_prospectdetail = relationship("TrxProspectDetail",back_populates="prospectdetail_accessories",foreign_keys="TrxProspectDetail.accessories_option_id")
