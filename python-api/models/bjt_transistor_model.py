from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class BjtTransistorModel(ComponentModel):
    __tablename__ = 'bjt_transistor'

    # Primary key
    id = Column(ForeignKey("component.id"), primary_key=True)

    # Specific properties of a BJT
    vce_sat_max = Column(String(30))
    hfe = Column(String(30))
    vce_max = Column(String(30))
    ic_max = Column(String(50))
    power_max = Column(String(50))
    bjt_type = Column(String(10))

    # Tells the ORM the type of a specific component by the distinguish column
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }
