from sqlalchemy import String, Column, Float, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrAddress(Base):
    __tablename__ = "mtr_address"
    is_active = Column(Boolean, nullable=False, default=True)
    address_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    address_latitude = Column(Float, nullable=True, default=0)
    address_longitude = Column(Float, nullable=True, default=0)
    address_street_1 = Column(String(100), nullable=False)
    address_street_2 = Column(String(100), nullable=False)
    address_street_3 = Column(String(100), nullable=False)
    address_type = Column(String(5), nullable=True, default="Test")
    village_id = Column(Integer, ForeignKey("mtr_village.village_id"))

    # back populates
    village_address = relationship(
        "MtrVillage", back_populates="address_village", foreign_keys=[village_id]
    )

    reference_address=relationship("MtrSupplierReferenceEntity",back_populates="address_reference",foreign_keys="MtrSupplierReferenceEntity.supplier_address_id")
    reference_vat_address=relationship("MtrSupplierReferenceEntity",back_populates="address_reference_vat",foreign_keys="MtrSupplierReferenceEntity.vat_address_id")
    reference_tax_address=relationship("MtrSupplierReferenceEntity",back_populates="address_reference_tax",foreign_keys="MtrSupplierReferenceEntity.tax_address_id")
    default_delivery_address=relationship("MtrCustomerDefaultDelivery",back_populates="address_default_delivery",foreign_keys="MtrCustomerDefaultDelivery.address_id")
    tax_office_address = relationship("MtrTaxServiceOffice",back_populates="address_tax_office",foreign_keys="MtrTaxServiceOffice.tax_service_office_Address_id")

    company_address = relationship(
        "MtrCompany",
        back_populates="address_company",
        foreign_keys="MtrCompany.company_office_address_id",
    )
    vat_address = relationship(
        "MtrVatCompany",
        back_populates="address_vat",
        foreign_keys="MtrVatCompany.vat_address_id",
    )
    tax_address = relationship(
        "MtrCompany",
        back_populates="address_tax",
        foreign_keys="MtrCompany.tax_address_id",
    )

    address_delivery_bfk = relationship(
        "MtrCustomerDeliveryAddress",
        back_populates="address_delivery_fk",
        foreign_keys="MtrCustomerDeliveryAddress.address_id",
    )
    id_address_bfk = relationship(
        "MtrCustomer",
        back_populates="id_address_fk",
        foreign_keys="MtrCustomer.id_address_id",
    )
    home_address_bfk = relationship(
        "MtrCustomer",
        back_populates="home_address_fk",
        foreign_keys="MtrCustomer.home_address_id",
    )
    office_address_bfk = relationship(
        "MtrCustomer",
        back_populates="office_address_fk",
        foreign_keys="MtrCustomer.office_address_id",
    )
    reference_address_bfk = relationship(
        "MtrCustomer",
        back_populates="reference_address_fk",
        foreign_keys="MtrCustomer.reference_address_id",
    )
    tax_address_bfk = relationship(
        "MtrCustomer",
        back_populates="tax_address_fk",
        foreign_keys="MtrCustomer.tax_address_id",
    )
    vat_address_bfk = relationship(
        "MtrCustomer",
        back_populates="vat_address_fk",
        foreign_keys="MtrCustomer.vat_address_id",
    )

    address_supplier = relationship(
        "MtrSupplier",
        back_populates="supplier_address",
        foreign_keys="MtrSupplier.supplier_address_id",
    )
    address_supplier_vat = relationship(
        "MtrSupplier",
        back_populates="supplier_vat_address",
        foreign_keys="MtrSupplier.vat_address_id",
    )
    address_supplier_tax = relationship(
        "MtrSupplier",
        back_populates="supplier_tax_address",
        foreign_keys="MtrSupplier.tax_address_id",
    )
