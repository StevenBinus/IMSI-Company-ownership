from sqlalchemy import String,Column,Integer,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrTaxServiceOffice(Base):
        __tablename__ = "mtr_tax_service_office"
        tax_service_office_id = Column(Integer,primary_key=True,nullable=False)
        tax_service_office_code = Column(String(10),nullable=False)
        tax_service_office_name = Column(String(100),nullable=False)
        tax_service_office_phone_no = Column(String(30),nullable=False)
        tax_service_office_Address_id = Column(Integer,ForeignKey("mtr_address.address_id"),nullable=False)
        address_tax_office = relationship("MtrAddress",back_populates="tax_office_address",foreign_keys=[tax_service_office_Address_id])

        #back populates
        tax_office_address= relationship("MtrSupplierReferenceEntity",back_populates="address_tax_office",foreign_keys="MtrSupplierReferenceEntity.tax_tax_service_office_id")
        vat_office_address= relationship("MtrSupplierReferenceEntity",back_populates="address_vat_office",foreign_keys="MtrSupplierReferenceEntity.vat_tax_service_office_id")