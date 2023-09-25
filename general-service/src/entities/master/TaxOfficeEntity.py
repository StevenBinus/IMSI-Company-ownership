from sqlalchemy import Boolean, String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrTaxOffice(Base):
    __tablename__ = "mtr_tax_office"
    is_active = Column(Boolean, nullable=False, default=True)
    tax_office_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True
    )
    tax_office_code = Column(String(10), nullable=False, unique=True)
    tax_office_name = Column(String(100), nullable=False, default="")
    tax_office_phone_no = Column(String(30), nullable=False, default="")
    tax_office_address_id = Column(Integer, ForeignKey("mtr_address.address_id"))

    # back populates
    company_taxoffice = relationship(
        "MtrCompany",
        back_populates="taxoffice_company",
        foreign_keys="MtrCompany.tax_office_id",
    )
    vatcompany_taxoffice = relationship(
        "MtrVatCompany",
        back_populates="taxoffice_vatcompany",
        foreign_keys="MtrVatCompany.vat_tax_office_id",
    )
    vat_kpp_id_bfk = relationship(
        "MtrCustomer",
        back_populates="vat_taxoffice_id_fk",
        foreign_keys="MtrCustomer.vat_tax_office_id",
    )
    taxoffice_id_bfk = relationship(
        "MtrCustomer",
        back_populates="tax_office_id_id_fk",
        foreign_keys="MtrCustomer.tax_office_id",
    )
