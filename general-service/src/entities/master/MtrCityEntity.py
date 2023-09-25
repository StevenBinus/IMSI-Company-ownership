from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCity(Base):
    __tablename__ = "mtr_city"
    is_active = Column(Boolean, nullable=False, default=True)
    city_id = Column(Integer, autoincrement=True,primary_key=True)
    city_code = Column(String(5),nullable=False,unique=True)
    city_name = Column(String(100), nullable=False)
    city_phone_area = Column(String(5), nullable=True)
    province_id = Column(Integer,ForeignKey("mtr_province.province_id",ondelete="CASCADE"))

    #back populates
    province_city = relationship("MtrProvince",back_populates="city_province", foreign_keys=[province_id])
    district_city = relationship("MtrDistrict",back_populates="city_district", foreign_keys="MtrDistrict.city_id")
    city_bfk = relationship("MtrCostProfitMap",back_populates="city_fk", foreign_keys="MtrCostProfitMap.city_id")
    village_city = relationship("MtrVillage",back_populates="city_village",foreign_keys="MtrVillage.city_id")
