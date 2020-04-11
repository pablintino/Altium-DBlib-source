from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .module_base import Base


class LibraryReference(Base):
    __tablename__ = "library_ref"
    id = Column(Integer, primary_key=True)
    symbol_path = Column(String(300))
    symbol_ref = Column(String(150))

    # relationships
    library_components = relationship("ComponentModel", back_populates='library_ref', lazy=True)

    def __repr__(self):
        return "LibraryReference %s %s" % (
            self.symbol_path,
            self.symbol_ref,
        )
