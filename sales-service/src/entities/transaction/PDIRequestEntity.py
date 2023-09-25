from src.configs.database import Base
from sqlalchemy import Column,String, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

class TrxPDIRequest(Base):
    __tablename__ = "trx_pdi_request"
    company_id = Column(Integer,nullable=False) # FK to mtr_company common-general service
    pdi_request_system_number = Column(Integer,primary_key=True,autoincrement=True)
    pdi_request_document_number = Column(String(25),unique=True,nullable=True)
    brand_id = Column(Integer,ForeignKey("mtr_brand.brand_id"),nullable=False)
    pdi_request_date = Column(DateTime,nullable=True)
    issued_by_id = Column(Integer,nullable=False) # FK to user service
    service_dealer_id = Column(Integer,nullable=True,default=0) # FK to mtr_supplier common-general service
    service_by_id = Column(Integer,nullable=False) # FK to user service
    pdi_request_remark = Column(String(256),nullable=True, default="")
    pdi_request_status_id = Column(Integer,nullable=False,default=0) # Fk to common-general service
    total_frt = Column(Float,nullable=True,default=0)
    # pdireq_brand = relationship("MtrBrand",back_populates="brand_pdireq",foreign_keys=[brand_id])