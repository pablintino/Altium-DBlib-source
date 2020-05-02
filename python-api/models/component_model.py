from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .module_base import Base
from .join_tables import component_footprint_asc_table


class ComponentModel(Base):
    __tablename__ = 'component'

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)

    # This column tells the ORM the specific component child type
    type = Column(String(50))

    # General component properties
    mpn = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    value = Column(String(100))
    package = Column(String(100))
    description = Column(String(200))
    comment = Column(String(100))

    # Relationships
    library_ref_id = Column(Integer, ForeignKey('library_ref.id'))
    library_ref = relationship('LibraryReference', back_populates="library_components", lazy='subquery')
    footprint_refs = relationship('FootprintReference', secondary=component_footprint_asc_table, lazy='subquery',
                                  back_populates='components_f')

    __mapper_args__ = {
        'polymorphic_identity': 'component',
        'polymorphic_on': type
    }

    # Set a constraint that enforces Part Number - Manufacturer uniqueness
    __table_args__ = (UniqueConstraint('mpn', 'manufacturer', name='_mpn_manufacturer_uc'),
                      )

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    @staticmethod
    def get_unique_constraints():
        return dict([(c.name, any([c.primary_key, c.unique])) for c in ComponentModel.__table__.columns])
