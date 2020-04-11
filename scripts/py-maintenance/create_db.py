from sqlalchemy import select, join
from sqlalchemy.orm import sessionmaker
from models import ResistorModel, LibraryReference, FootprintReference, ComponentModel, component_footprint_asc_table
from alchemy import encoders, session_manager, views
import json

Session = sessionmaker(session_manager.engine)
session = Session()

#session_manager.metadata.drop_all(session_manager.engine)

#stuff_view = views.view("resistor_view", session_manager.metadata,
#                        select(
#                            [
#                                ResistorModel.id,
#                                ResistorModel.tolerance,
#                                ResistorModel.power_max,
#                                ComponentModel.mpn,
#                                ComponentModel.manufacturer,
#                                ComponentModel.created_on,
#                                ComponentModel.updated_on,
#                                ComponentModel.type,
#                                ComponentModel.value,
#                                ComponentModel.package,
#                                ComponentModel.description,
#                                ComponentModel.comment,
#                            ]
#                        ).select_from(
#                            ResistorModel.__table__.join(ComponentModel).join(LibraryReference).join(
#                                component_footprint_asc_table).join(FootprintReference))
#                        )

session_manager.metadata.create_all(session_manager.engine)

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

print(json.dumps(session.query(ResistorModel).first(), cls=encoders.AlchemyEncoder))
