from sqlalchemy import String,Column,Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrSupplierPIC(Base):
    __tablename__ = "mtr_supplier_pic"
    supplier_pic_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pic_code = Column(String(5), nullable=False, unique=True)
    pic_name = Column(String(100), nullable=False)
    pic_division_id = Column(Integer, nullable=True) #Fk dari mtr_division sudah dibuat tapi belum di merge
    pic_job_title_id = Column(Integer, ForeignKey("mtr_job_title.job_title_id"), nullable=True)
    pic_mobile_phone = Column(String(30), nullable=True)
    supplier_id = Column(Integer, ForeignKey("mtr_supplier.supplier_id"), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    #back populates
    pic_job_title = relationship("MtrJobTitle", back_populates="job_title_pic", foreign_keys=[pic_job_title_id])
    pic_supplier = relationship("MtrSupplier", back_populates="supplier_pic", foreign_keys=[supplier_id])