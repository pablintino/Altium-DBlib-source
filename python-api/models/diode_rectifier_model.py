from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class DiodeRectifierModel(ComponentModel):
    __tablename__ = 'diode_rectifier'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a rectifier diode
    forward_voltage = Column(String(30))
    reverse_current_leakage = Column(String(30))
    max_forward_average_current = Column(String(30))
    max_reverse_vrrm = Column(String(30))
    diode_type = Column(String(50))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
