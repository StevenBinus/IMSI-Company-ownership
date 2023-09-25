from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrJobPosition(Base):
    __tablename__ = 'mtr_job_position'
    is_active = Column(Boolean, default=True, nullable=False)
    job_position_id = Column(Integer, autoincrement=True, primary_key=True)
    job_position_code = Column(String(10), nullable=False, unique=True)
    job_position_name = Column(String(256), nullable=False)

    #back populates
    reference_pic_job_position = relationship("MtrSupplierReferencePic",back_populates="job_position_reference_pic",foreign_keys="MtrSupplierReferencePic.pic_position_id")