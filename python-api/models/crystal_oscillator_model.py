from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class CrystalOscillatorModel(ComponentModel):
    __tablename__ = 'crystal_oscillator'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a crystal oscillator
    load_capacitance = Column(String(30))
    frequency = Column(String(30))
    frequency_tolerance = Column(String(30))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
