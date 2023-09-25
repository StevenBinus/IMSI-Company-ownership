from sqlalchemy import Column,String,Integer,Boolean,ForeignKey, Identity,UniqueConstraint
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCustomerBankAccount(Base):
    __tablename__ = "mtr_customer_bank_account"
    customer_bank_account_id  = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, default=True)
    customer_id = Column(Integer, ForeignKey("mtr_customer.customer_id"), nullable=False)
    bank_id = Column(Integer, nullable=False) # diambil dari table mtr_bank modul finance
    bank_account_type_id = Column(Integer, ForeignKey("mtr_bank_account_type.bank_account_type_id"), nullable=True, default=0)
    bank_account_name = Column(String(60), nullable=True, default="")
    bank_account_number = Column(String(20), nullable=False, unique=True)
    currency_id = Column(Integer, nullable=True, default=0) # diambil dari table mtr_currency modul finance

    
    __table_args__ = (UniqueConstraint('customer_id', 'bank_id', name='_unique_field_customer_bank'),)
    customer_bank_fk = relationship("MtrCustomer", back_populates="customer_bank_bfk", foreign_keys=[customer_id])
    bank_account_type_fk = relationship("MtrBankAccountType", back_populates="bank_account_type_bfk", foreign_keys=[bank_account_type_id])