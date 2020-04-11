from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class ResistorModel(ComponentModel):
    __tablename__ = 'resistor'
    id = Column(ForeignKey("component.id"), primary_key=True)
    power_max = Column(String(30))
    tolerance = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity': 'resistor',
    }

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
