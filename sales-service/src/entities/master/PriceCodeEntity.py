from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrPriceCode(Base):
    __tablename__ = "mtr_price_code"
    is_active = Column(Boolean,nullable=False,default=True)
    price_code_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    brand_id = Column(Integer,ForeignKey("mtr_brand.brand_id"),nullable=True)
    price_code = Column(String(10),nullable=False,unique=True)
    price_code_name = Column(String(50),nullable=True)
    price_code_customized =  Column(Boolean,nullable=True,default=False)
    price_code_modifiabled = Column(Boolean,nullable=True,default=False)
    price_code_otr_modifiabled = Column(Boolean,nullable=True,default=False)
    price_code_dp_modifiabled = Column(Boolean,nullable=True,default=False)
   
   
    #back populates
    pricecode_brand = relationship("MtrBrand",back_populates='brand_pricecode',foreign_keys=[brand_id])
    