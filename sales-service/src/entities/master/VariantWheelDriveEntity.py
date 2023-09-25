from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrVariantWheelDrive(Base):
    __tablename__ = "mtr_variant_wheel_drive"
    is_active = Column(Boolean,nullable=False,default=False)
    variant_wheel_drive_id = Column(Integer,primary_key=True,autoincrement=True)
    variant_wheel_drive_code = Column(String(5),unique=True,nullable=False)
    variant_wheel_drive_name = Column(String(30),nullable=False)
    #back populates
    wheeldrive_unitvariant = relationship("MtrUnitVariant",back_populates="unitvariant_wheeldrive",foreign_keys="MtrUnitVariant.wheel_drive_id")
