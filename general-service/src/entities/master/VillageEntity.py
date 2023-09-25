from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class  MtrVillage(Base):
    __tablename__ = "mtr_village"
    is_active = Column(Boolean, nullable=False, default=True)
    village_id = Column(Integer, autoincrement=True,primary_key=True)
    village_code = Column(String(5),nullable=False,unique=True)
    village_name = Column(String(100), nullable=False)
    village_zip_code = Column(String(10), nullable=False)
    district_id = Column(Integer,ForeignKey("mtr_district.district_id",ondelete="CASCADE"))
    city_id = Column (Integer,ForeignKey("mtr_city.city_id"))
    province_id = Column(Integer,ForeignKey("mtr_province.province_id"))

    #back populates
    district_village = relationship("MtrDistrict",back_populates="village_district", foreign_keys=[district_id])
    city_village=relationship("MtrCity",back_populates="village_city",foreign_keys=[city_id])
    province_city=relationship("MtrProvince",back_populates="village_province",foreign_keys=[province_id])
    village_kpp=relationship("MtrKpp",back_populates="kpp_village",foreign_keys="MtrKpp.village_id")
    address_village = relationship("MtrAddress",back_populates="village_address", foreign_keys="MtrAddress.village_id")