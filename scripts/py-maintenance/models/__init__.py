from .module_base import Base
from .join_tables import component_footprint_asc_table
from .library_reference_model import LibraryReference
from .footprint_reference_model import FootprintReference
from .resistor_model import ResistorModel
from .capacitor_model import CapacitorModel
from .diode_tvs_model import DiodeZenerModel
from .diode_zener_model import DiodeZenerModel
from .diode_rectifier_model import DiodeRectifierModel
from .power_inductor_model import PowerInductorModel
from .ferrite_bead_model import FerriteBeadModel
from .moset_transistor_model import MosfetTransistorModel
from .bjt_transistor_model import BjtTransistorModel
from .crystal_oscillator_model import CrystalOscillatorModel
from .component_model import ComponentModel
from models.metadata.model_descriptor import ModelDescriptor, FieldModelDescriptor
from .join_tables import component_footprint_asc_table
import alchemy
import configuration
import logging

__logger = logging.getLogger(__name__)


def init_database_models():
    if configuration.app_config['app']['init']['create_tables']:
        __logger.info("Application database is going to be self deployed")
        alchemy.metadata.create_all()


init_database_models()
