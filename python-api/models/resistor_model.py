from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class ResistorModel(ComponentModel):
    __tablename__ = 'resistor'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a resistor
    power_max = Column(String(30))
    tolerance = Column(String(30))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
