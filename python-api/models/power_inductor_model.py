from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class PowerInductorModel(ComponentModel):
    __tablename__ = 'power_inductor'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of an inductor
    tolerance = Column(String(30))
    resistance_dcr = Column(String(30))
    inductance_freq_test = Column(String(30))
    current_rating = Column(String(30))
    current_saturation = Column(String(30))
    core_material = Column(String(50))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
