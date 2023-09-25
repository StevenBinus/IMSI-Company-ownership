from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrModelVariantColour(Base):
    __tablename__ = "mtr_model_variant_colour"
    is_active = Column(Boolean, nullable=False, default=True)
    model_variant_colour_id = Column(
        Integer, nullable=False, primary_key=True, autoincrement=True
    )
    brand_id = Column(Integer, ForeignKey("mtr_brand.brand_id"), nullable=True)
    model_id = Column(Integer, ForeignKey("mtr_unit_model.model_id"), nullable=True)
    colour_id = Column(Integer, ForeignKey("mtr_colour.colour_id"), nullable=True)
    variant_id = Column(
        Integer, ForeignKey("mtr_unit_variant.variant_id"), nullable=True
    )
    model_variant_colour_name = Column(String(50), nullable=True, default="")
    model_variant_colour_description = Column(String(200), nullable=True, default="")
    model_variant_colour_sales_allow = Column(Boolean, nullable=True, default="")
    model_variant_colour_discontinue_date = Column(DateTime, nullable=True)
    model_variant_colour_incident_indicator = Column(Boolean, nullable=True, default="")
    model_variant_colour_option_code = Column(String(50), nullable=True, default="")
    model_variant_colour_hs_code = Column(String(10), nullable=True, default="")
    # back populates
    mvc_brand = relationship(
        "MtrBrand", back_populates="brand_mvc", foreign_keys=[brand_id]
    )
    mvc_model = relationship(
        "MtrUnitModel", back_populates="model_mvc", foreign_keys=[model_id]
    )
    mvc_colour = relationship(
        "MtrColour", back_populates="colour_mvc", foreign_keys=[colour_id]
    )
    mvc_variant = relationship(
        "MtrUnitVariant", back_populates="variant_mvc", foreign_keys=[variant_id]
    )
