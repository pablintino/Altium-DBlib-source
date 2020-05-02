from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class CapacitorModel(ComponentModel):
    __tablename__ = 'capacitor'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a capacitor
    tolerance = Column(String(30))
    voltage = Column(String(30))
    composition = Column(String(30))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
