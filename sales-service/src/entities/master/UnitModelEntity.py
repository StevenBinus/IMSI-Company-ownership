from sqlalchemy import Column, Boolean, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrUnitModel(Base):
    __tablename__ = "mtr_unit_model"
    is_active = Column(Boolean,nullable=False,default=True)
    model_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    vehicle_brand_id = Column(Integer,ForeignKey("mtr_brand.brand_id"))
    model_code = Column(String(25),nullable=False,unique=True)
    model_description = Column(String(35),nullable=False,default="")
    unit_group_id = Column(Integer,ForeignKey("mtr_unit_group.unit_group_id"))
    discontinue_date = Column(DateTime,nullable=False,default="")
    sales_allow = Column(Boolean,nullable=False,default=False)
    indent_indicator = Column(Boolean,nullable=False,default=False)
    warranty_expired_year = Column(Float,nullable=False,default=0)
    warranty_expired_mileage = Column(Float,nullable=False,default=0)
    free_service_expired_month = Column(Float,nullable=False,default=0)
    free_service_expired_mileage = Column(Float,nullable=False,default=0)
    #back populates
    model_brand = relationship("MtrBrand", back_populates="brand_model", foreign_keys=[vehicle_brand_id])
    model_unitgroup = relationship("MtrUnitGroup", back_populates="unitgroup_model", foreign_keys=[unit_group_id]) 
    model_mvc = relationship("MtrModelVariantColour", back_populates="mvc_model", foreign_keys="MtrModelVariantColour.model_id")
    model_prospectdetail = relationship("TrxProspectDetail", back_populates="prospectdetail_model",foreign_keys="TrxProspectDetail.prospect_model_id")
    model_unitvariant = relationship("MtrUnitVariant",back_populates="unitvariant_model",foreign_keys="MtrUnitVariant.model_id")
    
    model_vehicle = relationship("MtrVehicle",back_populates='vehicle_model',foreign_keys="MtrVehicle.vehicle_model_id")
