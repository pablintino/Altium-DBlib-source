from sqlalchemy.ext.declarative import declarative_base
from alchemy.session_manager import metadata

Base = declarative_base(metadata=metadata)
