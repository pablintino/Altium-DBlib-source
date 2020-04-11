from sqlalchemy import Column, String, ForeignKey
from .component_model import ComponentModel


class CapacitorModel(ComponentModel):
    __tablename__ = 'capacitor'
    id = Column(ForeignKey("component.id"), primary_key=True)
    tolerance = Column(String(30))
    voltage = Column(String(30))
    composition = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity': 'capacitor',
    }

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
