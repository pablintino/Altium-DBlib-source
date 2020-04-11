from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .join_tables import component_footprint_asc_table
from .module_base import Base


class FootprintReference(Base):
    __tablename__ = "footprint_ref"
    id = Column(Integer, primary_key=True)
    footprint_path = Column(String(300))
    footprint_ref = Column(String(150))

    # relationships
    components_f = relationship("ComponentModel",
                                secondary=component_footprint_asc_table,
                                back_populates="footprint_refs",
                                lazy=True)

    def __repr__(self):
        return "FootprintReference %s %s" % (
            self.footprint_path,
            self.footprint_ref,
        )
