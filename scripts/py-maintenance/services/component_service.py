from models.metadata import metadata_utils
import logging
import os

# TODO Remove this temp logging config from here
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
__logger = logging.getLogger(__name__)

# Stores components metadata to present it to api consumers
__component_metadata = {}


def create_component(component_dto):
    #TODO
    print(component_dto)


def get_component_types():
    global __component_metadata
    #    session = sessionmaker()
    __logger.debug("Retrieving component types...")
    #   component_types = session.query(ComponentModel.type).distinct(ComponentModel.type).all()
    component_types = list(__component_metadata.keys())
    __logger.debug("Retrieved %d component types", len(component_types))
    #    session.close()
    return component_types


def __init():
    global __component_metadata
    __component_metadata = metadata_utils.get_component_metadata()


# Initialize service instance
__init()
get_component_types()

