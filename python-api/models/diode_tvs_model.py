from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class DiodeZenerModel(ComponentModel):
    __tablename__ = 'diode_tvs'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a TVS diode
    voltage_reverse_standoff = Column(String(30))
    voltage_breakdown_min = Column(String(30))
    voltage_clamping_max = Column(String(30))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
