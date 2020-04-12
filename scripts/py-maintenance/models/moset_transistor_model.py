from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class MosfetTransistorModel(ComponentModel):
    __tablename__ = 'mosfet_transistor'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a MOSFET
    rds_on = Column(String(30))
    vgs_max = Column(String(30))
    vgs_th = Column(String(30))
    vds_max = Column(String(30))
    ids_max = Column(String(50))
    power_max = Column(String(50))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
