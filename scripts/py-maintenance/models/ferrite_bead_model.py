from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class FerriteBeadModel(ComponentModel):
    __tablename__ = 'ferrite_bead'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a ferrite bead
    number_of_lines = Column(String(30))
    dc_resistance = Column(String(30))
    impedance_freq = Column(String(30))
    current_rating = Column(String(30))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
