#
# MIT License
#
# Copyright (c) 2020 Pablo Rodriguez Nava, @pablintino
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#


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
