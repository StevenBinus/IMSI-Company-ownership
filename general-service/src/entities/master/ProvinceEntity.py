from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrProvince(Base):
    __tablename__ = "mtr_province"
    is_active = Column(Boolean, nullable=False, default=True)
    province_id = Column(Integer,primary_key=True)
    province_code = Column(String(5),nullable=False,unique=True)
    province_name = Column(String(100), nullable=False)
    country_id = Column(Integer,ForeignKey("mtr_country.country_id"))

    #back populates
    country_province = relationship("MtrCountry",back_populates="province_country",foreign_keys=[country_id])
    city_province = relationship("MtrCity",back_populates="province_city", foreign_keys="MtrCity.province_id")
    district_province=relationship("MtrDistrict",back_populates="province_district",foreign_keys="MtrDistrict.province_id")
    village_province=relationship("MtrVillage",back_populates="province_city",foreign_keys="MtrVillage.province_id")  

    # city_province = relationship("MtrCity",back_populates="province_city", foreign_keys="MtrCity.province_id")
