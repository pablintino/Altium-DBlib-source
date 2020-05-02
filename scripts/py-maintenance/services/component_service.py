import logging
import os

# TODO Remove this temp logging config from here
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
__logger = logging.getLogger(__name__)


def create_component(component_dto):
    #TODO
    print(component_dto)

