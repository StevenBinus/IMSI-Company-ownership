from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrColour(Base):
    __tablename__ = "mtr_colour"
    is_active = Column(Boolean, nullable=False, default=True)
    colour_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    colour_code = Column(String(100), nullable=False, unique=True)
    colour_commercial_name = Column(String(100), nullable=True, default="")
    colour_police_name = Column(String(100), nullable=True, default="")
    brand_id = Column(Integer, ForeignKey("mtr_brand.brand_id"))
    # back populates
    colour_brand = relationship(
        "MtrBrand", back_populates="brand_colour", foreign_keys=[brand_id]
    )
    colour_mvc = relationship(
        "MtrModelVariantColour",
        back_populates="mvc_colour",
        foreign_keys="MtrModelVariantColour.colour_id",
    )
    colour_prospectdetail = relationship(
        "TrxProspectDetail",
        back_populates="prospectdetail_colour",
        foreign_keys="TrxProspectDetail.prospect_colour_id",
    )
