from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship
from src.configs.database import Base


class MtrBrand(Base):
    __tablename__ = "mtr_brand"
    is_active = Column(Boolean, nullable=False, default=True)
    brand_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(
        Integer, nullable=False
    )  # FK with general/master service and connect using API/RabbitMQ (event-driven SAGA Pattern)
    warehouse_id = Column(
        Integer, nullable=False
    )  # FK with aftersales service and connect using API/RabbitMQ (event-driven SAGA Pattern)
    brand_code = Column(String(6), nullable=False, unique=True)
    brand_name = Column(String(50), nullable=False, default="")
    brand_abbreviation = Column(String(3), nullable=False)
    brand_must_withdrawl = Column(Boolean, nullable=False, default=False)
    brand_must_pdi = Column(Boolean, nullable=False, default=False)
    atpm_unit = Column(Boolean, nullable=False, default=False)
    atpm_workshop = Column(Boolean, nullable=False, default=False)
    atpm_sparepart = Column(Boolean, nullable=False, default=False)
    atpm_finance = Column(Boolean, nullable=False, default=False)
    # back populates
    brand_spm_take = relationship(
        "TrxVehicleSalesOrderTake",
        back_populates="spm_take_brand",
        foreign_keys="TrxVehicleSalesOrderTake.brand_id",
    )
    brand_colour = relationship(
        "MtrColour", back_populates="colour_brand", foreign_keys="MtrColour.brand_id"
    )
    brand_mvc = relationship(
        "MtrModelVariantColour",
        back_populates="mvc_brand",
        foreign_keys="MtrModelVariantColour.brand_id",
    )
    brand_prospectdetail = relationship(
        "TrxProspectDetail",
        back_populates="prospectdetail_brand",
        foreign_keys="TrxProspectDetail.prospect_brand_id",
    )
    brand_model = relationship(
        "MtrUnitModel",
        back_populates="model_brand",
        foreign_keys="MtrUnitModel.vehicle_brand_id",
    )
