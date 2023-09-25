from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrJobTitle(Base):
    __tablename__ = 'mtr_job_title'
    is_active = Column(Boolean, default=True, nullable=False)
    job_title_id = Column(Integer, autoincrement=True, primary_key=True)
    job_title_code = Column(String(5), nullable=False, unique=True)
    job_title_name = Column(String(100), nullable=False)

    #back populates
    Jobtitle_bfk = relationship("MtrCustomerDeliveryAddress", back_populates="Jobtitle_fk",foreign_keys="MtrCustomerDeliveryAddress.job_title_id")
    job_title_pic = relationship("MtrSupplierPIC", back_populates="pic_job_title", foreign_keys="MtrSupplierPIC.pic_job_title_id")
    customer_job_title_bfk = relationship("MtrCustomer", back_populates="customer_job_title_fk", foreign_keys="MtrCustomer.customer_job_title_id")
