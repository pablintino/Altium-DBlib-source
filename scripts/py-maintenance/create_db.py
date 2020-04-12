from sqlalchemy.orm import sessionmaker
from models import ResistorModel, LibraryReference, FootprintReference, ComponentModel, component_footprint_asc_table
import alchemy
import json

Session = sessionmaker(alchemy.engine)
session = Session()

alchemy.metadata.drop_all(alchemy.engine)
alchemy.metadata.create_all(alchemy.engine)

# Create
library_ref = LibraryReference(symbol_path='path_test', symbol_ref='symbol_ref_test')
footprint_ref1 = FootprintReference(footprint_path='path_test', footprint_ref='ref_test')
footprint_ref2 = FootprintReference(footprint_path='path_test2', footprint_ref='ref_test2')
resistor_example = ResistorModel(
    mpn="test3",
    manufacturer="test",
    power_max="test",
    value='20k',
    library_ref=library_ref,
    footprint_refs=[footprint_ref1, footprint_ref2]
)
resistor_example = ResistorModel(
    mpn="test2",
    manufacturer="test",
    power_max="test",
    value='10k',
    library_ref=library_ref,
    footprint_refs=[footprint_ref1, footprint_ref2]
)

session.add(resistor_example)
session.commit()

print(json.dumps(session.query(ResistorModel).first(), cls=alchemy.AlchemyEncoder))
