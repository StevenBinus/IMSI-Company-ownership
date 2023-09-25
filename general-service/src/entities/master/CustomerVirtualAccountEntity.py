from sqlalchemy import Identity,String,Column,Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerVirtualAccount(Base):
    __tablename__ = "mtr_customer_virtual_account_dbs"
    is_active = Column(Boolean, nullable=True, default=True)
    virtual_account_system_number_new = Column(Integer,Identity(start=1, increment=1),primary_key=True,nullable=False)
    virtual_account_system_number_old = Column(Integer,nullable=True)
    customer_id = Column(Integer, ForeignKey("mtr_customer.customer_id"), nullable=True)
    company_id = Column(Integer, ForeignKey("mtr_company.company_id"), nullable=True)
    account_bank_company = Column(Integer, nullable=True) #Table Relasi dari Finance Service
    customer_virtual_account = Column(String(20), nullable=True, unique=True)
    approval_dbs = Column(Integer, ForeignKey("mtr_approval_status.approval_status_id"), nullable=False)
    respons_dbs = Column(String(512),nullable=True, default="") 
    profit_center_id = Column(Integer, ForeignKey("mtr_profit_center.profit_center_id"), nullable=False)

    #back populates
    customer_virtual_account_fk = relationship("MtrCustomer",back_populates="customer_virtual_account_bfk", foreign_keys=[customer_id])
    company_customer_va_fk = relationship("MtrCompany",back_populates="company_customer_va_bfk", foreign_keys=[company_id])
    virtual_account_profit= relationship("MtrProfitCenter",back_populates="profit_virtual_account", foreign_keys=[profit_center_id])
    approval_fk= relationship("MtrApprovalStatus",back_populates="approval_bfk", foreign_keys=[approval_dbs])