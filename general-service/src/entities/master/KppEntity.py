from sqlalchemy import Boolean, String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base,engine

class MtrKpp(Base):
    __tablename__ = "mtr_kpp"
    is_active = Column(Boolean,nullable=False,default=True)
    kpp_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    kpp_code = Column(String(5),nullable=False,unique=True)
    kpp_name = Column(String(100),nullable=True,default="")
    kpp_phone_no = Column(String(14),nullable=True,default="")
    kpp_address_1 = Column(String(50),nullable=False)
    kpp_address_2 = Column(String(50),nullable=True)
    kpp_address_3 = Column(String(50),nullable=True)
    village_id = Column(Integer,ForeignKey("mtr_village.village_id",ondelete="CASCADE"))

    kpp_village = relationship("MtrVillage",back_populates="village_kpp",foreign_keys=[village_id])
  
    #back populates
    # company_kpp = relationship("MtrCompany",back_populates="kpp_company",foreign_keys="MtrCompany.tax_kpp_id")
    # vat_company_kpp = relationship("MtrVatCompany",back_populates="kpp_vat_company",foreign_keys="MtrVatCompany.vat_kpp_id")
    #customer_vat_kpp_id_bfk = relationship("MtrCustomer", back_populates="vat_kpp_id_fk", foreign_keys="MtrCustomer.vat_kpp_id")
    #kpp_id_bfk = relationship("MtrCustomer", back_populates="kpp_id_fk", foreign_keys="MtrCustomer.kpp_id")
