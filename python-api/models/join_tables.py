from sqlalchemy import Column, Integer, ForeignKey, Table
from .module_base import Base

component_footprint_asc_table = Table('component_footprint_asc', Base.metadata,
                                      Column('component_id', Integer, ForeignKey('component.id')),
                                      Column('footprint_ref_id', Integer, ForeignKey('footprint_ref.id'))
                                      )
