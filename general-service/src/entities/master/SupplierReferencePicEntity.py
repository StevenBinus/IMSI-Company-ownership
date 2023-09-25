from sqlalchemy import String,Column,Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrSupplierReferencePic(Base):
    __tablename__ = "mtr_supplier_reference_pic"
    supplier_reference_pic_id = Column(Integer,primary_key=True,nullable=False)
    pic_code = Column(String(5),nullable=False)
    pic_name = Column(String(100),nullable=False)
    pic_division_id = Column(Integer,ForeignKey("mtr_division.division_id"),nullable=True)
    pic_position_id = Column(Integer,ForeignKey("mtr_job_position.job_position_id"),nullable=True)
    pic_mobile_phone=Column(String(30),nullable=True)
    is_active = Column(Boolean,nullable=False,default=True)
    supplier_reference_id = Column(Integer,ForeignKey("mtr_supplier_reference.supplier_reference_id"),nullable=False)

    #back populates
    division_reference_pic = relationship("MtrDivision",back_populates="reference_pic_division",foreign_keys=[pic_division_id])
    job_position_reference_pic = relationship("MtrJobPosition",back_populates="reference_pic_job_position",foreign_keys=[pic_position_id])
    supplier_reference_pic_reference=relationship("MtrSupplierReferenceEntity",back_populates="reference_pic_reference",foreign_keys=[supplier_reference_id])
