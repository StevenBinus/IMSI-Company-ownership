from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrDistrict(Base):
    __tablename__ = "mtr_district"
    is_active = Column(Boolean, nullable=False, default=True)
    district_id = Column(Integer, autoincrement=True,primary_key=True)
    district_code = Column(String(5),nullable=False,unique=True)
    district_name = Column(String(100), nullable=False)
    city_id = Column(Integer,ForeignKey("mtr_city.city_id",ondelete="CASCADE"))
    province_id = Column(Integer,ForeignKey("mtr_province.province_id"))
    province_district=relationship("MtrProvince",back_populates="district_province",foreign_keys=[province_id])

    #back populates
    city_district = relationship("MtrCity",back_populates="district_city", foreign_keys=[city_id])
    village_district = relationship("MtrVillage",back_populates="district_village", foreign_keys="MtrVillage.district_id")