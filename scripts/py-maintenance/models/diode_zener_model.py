from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class DiodeZenerModel(ComponentModel):
    __tablename__ = 'diode_zener'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a zener diode
    tolerance = Column(String(30))
    power_max = Column(String(30))
    voltage_forward = Column(String(30))
    voltage_zener = Column(String(30))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
