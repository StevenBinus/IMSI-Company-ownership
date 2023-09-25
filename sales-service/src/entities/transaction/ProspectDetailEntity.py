from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base

class TrxProspectDetail(Base):
    __tablename__ = "trx_prospect_detail"
    prospect_detail_system_number = Column(Integer,primary_key=True,autoincrement=True)
    prospect_system_number = Column(Integer,ForeignKey("trx_prospect.prospect_system_number"))
    prospect_brand_id = Column(Integer,ForeignKey("mtr_brand.brand_id"))
    prospect_model_id = Column(Integer,ForeignKey("mtr_unit_model.model_id"))
    prospect_variant_id = Column(Integer,ForeignKey("mtr_unit_variant.variant_id"))
    prospect_colour_id = Column(Integer,ForeignKey("mtr_colour.colour_id"))
    prospect_quantity = Column(Integer,nullable=False)
    expected_delivery_date = Column(DateTime,nullable=True,default="")
    accessories_option_id = Column(Integer,ForeignKey("mtr_accessories_option.accessories_option_id"))
    #back populates
    prospectdetail_prospect = relationship("TrxProspectHeader",back_populates="prospect_prospectdetail",foreign_keys=[prospect_system_number])
    prospectdetail_brand = relationship("MtrBrand",back_populates="brand_prospectdetail",foreign_keys=[prospect_brand_id])
    prospectdetail_model = relationship("MtrUnitModel",back_populates="model_prospectdetail",foreign_keys=[prospect_model_id])
    prospectdetail_variant = relationship("MtrUnitVariant",back_populates="variant_prospectdetail",foreign_keys=[prospect_variant_id])
    prospectdetail_colour = relationship("MtrColour",back_populates="colour_prospectdetail",foreign_keys=[prospect_colour_id])
    prospectdetail_accessories = relationship("MtrAccessoriesOption",back_populates="accessories_prospectdetail",foreign_keys=[accessories_option_id])
