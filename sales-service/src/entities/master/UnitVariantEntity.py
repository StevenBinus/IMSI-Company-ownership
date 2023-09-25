from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrUnitVariant(Base):
    __tablename__ = "mtr_unit_variant"
    is_active = Column(Boolean,nullable=False,default=True)
    variant_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    model_id = Column(Integer,ForeignKey("mtr_unit_model.model_id"),nullable=False)
    variant_code = Column(String(25),nullable=False,unique=True)
    variant_description = Column(String(50),nullable=False,default="")
    release_date = Column(DateTime,nullable=True,default="")
    discontinue_date = Column(DateTime,nullable=True,default="")
    chassis_prefix = Column(String(15),nullable=True,default="")
    engine_prefix = Column(String(15),nullable=True,default="")
    production_year = Column(String(4),nullable=False)
    sales_allow = Column(Boolean,nullable=False,default=False)
    indent_indicator = Column(Boolean,nullable=False,default=False)
    dp_amount = Column(Float,nullable=False,default=True)
    cylinder_id = Column(Integer,ForeignKey("mtr_variant_cylinder.variant_cylinder_id"))
    fuel_id = Column(Integer,ForeignKey("mtr_variant_fuel.variant_fuel_id"))
    unit_type_id = Column(Integer,ForeignKey("mtr_variant_unit_type.variant_unit_type_id"))
    transmission_id = Column(Integer,ForeignKey("mtr_variant_transmission.variant_transmission_id"))
    wheel_drive_id = Column(Integer,ForeignKey("mtr_variant_wheel_drive.variant_wheel_drive_id"))
    vehicle_type_police_invoice = Column(String(100),nullable=True)
    vehicle_kind_police_invoice = Column(String(200),nullable=True)
    SUT = Column(String(100),nullable=True,default="")  
    price = Column(Float,nullable=True)
    #back populates
    unitvariant_model = relationship("MtrUnitModel",back_populates="model_unitvariant",foreign_keys=[model_id])
    unitvariant_cylinder = relationship("MtrVariantCylinder",back_populates="cylinder_unitvariant",foreign_keys=[cylinder_id])
    unitvariant_fuel = relationship("MtrVariantFuel",back_populates="fuel_unitvariant",foreign_keys=[fuel_id])
    unitvariant_unittype = relationship("MtrVariantUnitType",back_populates="unittype_unitvariant",foreign_keys=[unit_type_id])
    unitvariant_transmission = relationship("MtrVariantTransmission",back_populates="transmission_unitvariant",foreign_keys=[transmission_id])
    unitvariant_wheeldrive = relationship("MtrVariantWheelDrive",back_populates="wheeldrive_unitvariant",foreign_keys=[wheel_drive_id])
    
    variant_mvc = relationship("MtrModelVariantColour",back_populates='mvc_variant',foreign_keys="MtrModelVariantColour.variant_id")
    variant_prospectdetail = relationship("TrxProspectDetail",back_populates="prospectdetail_variant",foreign_keys="TrxProspectDetail.prospect_variant_id")
    variant_vehicle = relationship("MtrVehicle",back_populates='vehicle_variant',foreign_keys="MtrVehicle.vehicle_variant_id")
    