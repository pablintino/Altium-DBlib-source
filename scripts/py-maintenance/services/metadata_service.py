from models.metadata import metadata_utils
from services.exceptions import ResourceNotFoundError
import logging

__logger = logging.getLogger(__name__)

# Stores components metadata to present it to api consumers
__component_metadata = {}


## TODO TO BE DELETED HERE AS OLD QUERY EXAMPLE
def get_component_types():
    global __component_metadata
    #    session = sessionmaker()
    __logger.debug("Retrieving component types...")
    #   component_types = session.query(ComponentModel.type).distinct(ComponentModel.type).all()
    component_types = list(__component_metadata.keys())
    __logger.debug("Retrieved %d component types", len(component_types))
    #    session.close()
    return component_types


def get_component_metadata():
    items = []
    for comp_name, comp_type in __component_metadata.items():
        items.append(comp_type)
    return items


def __init():
    global __component_metadata
    __component_metadata = metadata_utils.get_component_metadata()


# Initialize service instance
__init()
