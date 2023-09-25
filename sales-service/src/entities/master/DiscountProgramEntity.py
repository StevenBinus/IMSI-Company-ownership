from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrDiscountProgram(Base):
    __tablename__ = "mtr_discount_program"
    is_active = Column(Boolean,nullable=False,default=True)
    discount_program_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    company_id = Column(Integer,nullable=False) # FK with general service mtr_company
    supplier_id = Column(Integer,nullable=False) # FK with general service mtr_suppplier    
    brand_id = Column(Integer,ForeignKey("mtr_brand.brand_id"))
    supplier_reference_document_number = Column(String(50),nullable=True,default="")
    supplier_reference_date = Column(DateTime,nullable=True,default="")
    efficient_date = Column(DateTime,nullable=True,default="")  
    max_request_date = Column(DateTime,nullable=True,default="")
    program_status = Column(String(2),nullable=True,default="")
    document_number = Column(String(25),nullable=True,default="")
    document_date = Column(DateTime,nullable=True,default="")
    remark = Column(String(255),nullable=True,default="")
    approval_request_number = Column(Float,nullable=True,default=0)
    approval_request_user = Column(Integer,nullable=False)
    approval_request_date = Column(DateTime,nullable=True,default="")
    approval_request_remark = Column(String(255),nullable=True,default="")
    approval_request_last_user = Column(Integer,nullable=False)
    approval_request_last_date = Column(DateTime,nullable=True,default="")