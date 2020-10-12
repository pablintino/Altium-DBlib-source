# dici Database Internal Component Identifier
import string
import random

from app import db
from models.components.component_model import ComponentModel
from models.inventory.inventory_identificable_item_model import InventoryIdentificableItemModel
from models.inventory.inventory_item_model import InventoryItemModel
from models.inventory.inventory_location import InventoryLocationModel


def __id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_item_id(obj_model=None):
    if isinstance(obj_model, InventoryIdentificableItemModel):
        model_prefix = obj_model.get_id_prefix()

        if isinstance(obj_model, InventoryItemModel) or isinstance(obj_model, ComponentModel):
            query_obj = InventoryItemModel
        elif isinstance(obj_model, InventoryLocationModel):
            query_obj = InventoryLocationModel
        else:
            query_obj = None

        if query_obj:
            for x in range(3):
                gen_dici = model_prefix + '-' + __id_generator()
                if not db.session.query(query_obj.dici).filter_by(dici=gen_dici).scalar():
                    return gen_dici
    else:
        return 'ITEM-' + __id_generator()

    return None
