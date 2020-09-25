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


from app import db
from models.inventory.inventory_item_model import InventoryItemModel
import logging

from models.inventory.inventory_item_stock import InventoryItemStockModel
from models.inventory.inventory_location import InventoryLocationModel
from utils.dici_utils import generate_item_id
from utils.helpers import BraceMessage as __l
from services.exceptions import ResourceAlreadyExistsApiError, UniqueIdentifierCreationError, ResourceNotFoundApiError, \
    RemainingStocksExistError

__logger = logging.getLogger(__name__)



def __gen_dici(model):
    # Create the ID that will identify the item/component for the rest of its life cycle
    dici_id = generate_item_id(model)
    if not dici_id:
        raise UniqueIdentifierCreationError("Cannot create a unique identifier for an inventory item")
    return dici_id


def create_item_for_component(component_model, auto_commit=False):
    exists_id = db.session.query(InventoryItemModel.id).filter_by(mpn=component_model.mpn,
                                                                  manufacturer=component_model.manufacturer).scalar()
    if exists_id:
        raise ResourceAlreadyExistsApiError(msg="An item already exists for the given component",
                                            conflicting_id=exists_id)

    item_model = InventoryItemModel(
        dici=__gen_dici(component_model),
        mpn=component_model.mpn,
        manufacturer=component_model.manufacturer,
        name=component_model.mpn,
        description=component_model.description,
        last_buy_price=0.0,
        component_id=component_model.id,
        component=component_model
    )

    db.session.add(item_model)

    # If autocommit persist the object right now
    if auto_commit:
        db.session.commit()

    __logger.debug(__l('Inventory item created [id={0}, dici={1}]', item_model.id, item_model.dici))
    return item_model


def get_item(item_id):
    __logger.debug(__l('Querying item data [item_id={0}]', item_id))
    item = InventoryItemModel.query.get(item_id)
    if not item:
        raise ResourceNotFoundApiError('Item not found', missing_id=item_id)

    return item


def create_location(name, description):
    location = InventoryLocationModel(name=name, description=description)
    location.dici = __gen_dici(location)

    db.session.add(location)
    db.session.commit()

    __logger.debug(__l('Inventory location created [id={0}, dici={1}]', location.id, location.dici))
    return location


def get_location(location_id):
    __logger.debug(__l('Querying location [location_id={0}]', location_id))
    item = InventoryLocationModel.query.get(location_id)
    if not item:
        raise ResourceNotFoundApiError('Location not found', missing_id=location_id)

    return item


def create_item_stocks_for_locations(item_id, location_ids):
    __logger.debug(__l('Creating new item-location relations [item_id={0}, footprint_ids={1}]', item_id,
                       location_ids))
    item = InventoryItemModel.query.get(item_id)
    item_stocks = []

    # Verify that the given item exists before trying anything else
    if not item:
        raise ResourceNotFoundApiError('Inventory item not found', missing_id=item_id)

    # Add only the locations that are not already associated
    locations_to_add = [location_id for location_id in location_ids if
                        location_id not in [cfr.location_id for cfr in item.stock_items]]

    try:

        for location_id in locations_to_add:
            location_model = InventoryLocationModel.query.get(location_id)
            if location_model:
                # Create a freshly new stock item for the location
                item_stock = InventoryItemStockModel(
                    actual_stock=0,
                    stock_min_level=0,
                    stock_notify_min_level=-1.0,
                    location_id=location_model.id,
                    location=location_model,
                    item_id=item.id,
                    item=item
                )
                item_stocks.append(item_stock)
                db.session.add(item_stock)
            else:
                raise ResourceNotFoundApiError('Inventory location not found', missing_id=location_id)

        item.stock_items.extend(item_stocks)
        db.session.add(item)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    __logger.debug(__l('Item locations updated [item_id={0}, location_ids={1}]', item_id, location_ids))
    return [cfr.location_id for cfr in item.stock_items]


def delete_stock_location(location_id):
    location = InventoryLocationModel.query.get(location_id)
    if location:
        if len([si for si in location.stock_items if si.actual_stock != 0]) > 0:
            raise RemainingStocksExistError("Location still contains available stocks")

        try:
            for stock_item in location.stock_items:
                db.session.delete(stock_item)

            db.session.delete(location)
            db.session.commit()

        except:
            db.session.rollback()

        __logger.debug(__l('Removed location [location_id={0}]', location_id))
