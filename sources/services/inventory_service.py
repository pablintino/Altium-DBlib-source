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


import logging

from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from app import db
from models.internal.internal_inventory_models import InventoryItemStockStatus, InventoryMassStockMovementResult
from models.inventory.inventory_item_model import InventoryItemModel
from models.inventory.inventory_item_location_stock import InventoryItemLocationStockModel
from models.inventory.inventory_item_property import InventoryItemPropertyModel
from models.inventory.inventory_item_stock_movement import InventoryItemLocationStockMovementModel
from models.inventory.inventory_location import InventoryLocationModel
from utils.dici_utils import generate_item_id
from utils.helpers import BraceMessage as __l
from services.exceptions import ResourceAlreadyExistsApiError, UniqueIdentifierCreationError, ResourceNotFoundApiError, \
    RemainingStocksExistError, InvalidMassStockUpdateError, MalformedSearchQueryError

__logger = logging.getLogger(__name__)


def __search_item_location_stock_by_ids_dicis(item_id=None, item_dici=None, location_id=None, location_dici=None):
    if not item_id and not item_dici:
        raise InvalidMassStockUpdateError('Inventory item should contain at least ID or DICI')
    if not location_id and not location_dici:
        raise InvalidMassStockUpdateError('Inventory location should contain at least ID or DICI')

    item_filters = []
    location_filters = []
    if location_id:
        location_filters.append(getattr(InventoryLocationModel, "id") == location_id)
    else:
        location_filters.append(getattr(InventoryLocationModel, "dici") == location_dici)

    if item_id:
        item_filters.append(getattr(InventoryItemModel, "id") == item_id)
    else:
        item_filters.append(getattr(InventoryItemModel, "dici") == item_dici)

    try:

        return InventoryItemLocationStockModel.query.join(InventoryItemModel).join(InventoryLocationModel).filter(
            *(item_filters + location_filters)).one()

    except NoResultFound:
        if InventoryItemModel.query.filter(*item_filters).count() == 0:
            # Item not exist
            raise ResourceNotFoundApiError("Item doesn't exist", missing_dici=item_dici, missing_id=item_id)

        if InventoryLocationModel.query.filter(*location_filters).count() == 0:
            # Location not exist
            raise ResourceNotFoundApiError("Location doesn't exist", missing_dici=location_dici, missing_id=location_id)

    except MultipleResultsFound:
        raise InvalidMassStockUpdateError('Internal integrity error')


def __update_item_location_stock(stock_item, quantity, reason):
    if stock_item.stock_min_level <= (stock_item.actual_stock + quantity):
        stock_item.actual_stock = stock_item.actual_stock + quantity

        stock_item_movement = InventoryItemLocationStockMovementModel(stock_change=quantity,
                                                                      reason=reason,
                                                                      stock_item_id=stock_item.id)
        return stock_item_movement

    else:
        raise InvalidMassStockUpdateError(
            __l('Item has reached its minimum stock level [item_dici={0}, location_dici={1}]',
                stock_item.item.dici,
                stock_item.location.dici))


def __get_item_location_stock(item_id, location_id):
    item_stock = InventoryItemLocationStockModel.query.filter_by(item_id=item_id, location_id=location_id).first()

    # Verify that the given item exists before trying anything else
    if not item_stock:

        # Try to raise a fine grade exception instead of the simplest one
        if not InventoryItemModel.query.get(item_id):
            raise ResourceNotFoundApiError('Inventory item not found', missing_id=item_id)
        if not InventoryItemModel.query.get(item_id):
            raise ResourceNotFoundApiError('Inventory location not found', missing_id=location_id)

    return item_stock


def __gen_dici(model):
    # Create the ID that will identify the item/component for the rest of its life cycle
    dici_id = generate_item_id(model)
    if not dici_id:
        raise UniqueIdentifierCreationError("Cannot create a unique identifier for an inventory item")
    return dici_id


def __check_item_existance(item_id):
    return db.session.query(InventoryItemModel.id).filter_by(id=item_id).scalar() is not None


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


def get_item_component(item_id):
    __logger.debug(__l('Querying item component [item_id={0}]', item_id))
    item = InventoryItemModel.query.get(item_id)
    if not item:
        raise ResourceNotFoundApiError('Item not found', missing_id=item_id)

    if not item.component:
        raise ResourceNotFoundApiError('Item has no component', missing_id=item_id)

    return item.component


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
                item_stock = InventoryItemLocationStockModel(
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


def get_item_stock_for_location(item_id, location_id):
    __logger.debug(__l('Retrieving item stock for location [item_id={0}, location_id={1}]', item_id, location_id))

    return __get_item_location_stock(item_id, location_id)


def update_item_location_stock_levels(item_id, location_id, min_stock_level=None, min_notify_level=None):
    __logger.debug(__l(
        'Updating item stock for location [item_id={0}, location_id={1}, min_stock_level={2}, min_notify_level={3}]',
        item_id, location_id, min_stock_level, min_notify_level))

    item_stock = __get_item_location_stock(item_id, location_id)
    if (min_stock_level is not None) and min_stock_level >= -1.0:
        item_stock.stock_min_level = min_stock_level
    if (min_notify_level is not None) and min_notify_level > -1.0:
        item_stock.stock_notify_min_level = min_notify_level

    db.session.add(item_stock)
    db.session.commit()

    return item_stock


def stock_mass_update(mass_stock_update):
    stock_status_lines = []
    try:
        for itm in mass_stock_update.movements:
            # Search the stock item location model by item/location id or dici
            stock_item = __search_item_location_stock_by_ids_dicis(item_id=itm.item_id, item_dici=itm.item_dici,
                                                                   location_id=itm.location_id,
                                                                   location_dici=itm.location_dici)

            # Annotate the stock movement
            movement_entry = __update_item_location_stock(stock_item, itm.quantity, mass_stock_update.reason)

            # Add DB changes to be persisted
            db.session.add(movement_entry)
            db.session.add(stock_item)

            # Append the change to a list to return the actual stock level to caller
            stock_status_lines.append(InventoryItemStockStatus(stock_level=stock_item.actual_stock,
                                                               item_dici=stock_item.item.dici,
                                                               location_dici=stock_item.location.dici))

        # Persist all the changes
        db.session.commit()

        __logger.debug(__l('Mass stock update done. {0} update movements executed.', len(stock_status_lines)))

        return InventoryMassStockMovementResult(stock_status_lines)

    except Exception as err:
        __logger.debug(__l('Mass stock aborted by {0}', err.__class__.__name__))

        # If a single operation goes wrong just rollback all changes
        db.session.rollback()
        raise


def add_property_to_item(item_id, property_model):
    __logger.debug(__l(
        'Adding property to item [item_id={0}, property_name={1},]', item_id, property_model.property_name))
    if not __check_item_existance(item_id):
        raise ResourceNotFoundApiError('Inventory item not found', missing_id=item_id)

    prop = InventoryItemPropertyModel.query.filter_by(property_name=property_model.property_name,
                                                      item_id=item_id).first()
    if prop:
        # Already exists
        raise ResourceAlreadyExistsApiError('Property already exists', conflicting_id=prop.id)

    property_model.item_id = item_id
    db.session.add(property_model)
    db.session.commit()

    return property_model


def update_item_property(item_id, property_id, new_value):
    __logger.debug(__l(
        'Updating item property [item_id={0}, property_id={1}]', item_id, property_id))

    prop = InventoryItemPropertyModel.query.get(property_id)
    if not prop:
        # Property not exists
        raise ResourceNotFoundApiError('Inventory property not found', missing_id=property_id)

    # Update model value
    prop.set_value(new_value)

    # Persist to DB
    db.session.add(prop)
    db.session.commit()

    return prop


def get_item_properties(item_id):
    __logger.debug(__l('Retrieving item properties [item_id={0}]', item_id))

    item = get_item(item_id)
    if not item:
        # Item not exists
        raise ResourceNotFoundApiError('Inventory item not found', missing_id=item_id)

    return item.item_properties


def delete_item_property(item_id, prop_id):
    __logger.debug(__l('Removed item property [item_id={0}, prop_id={1}]', item_id, prop_id))
    prop = InventoryItemPropertyModel.query.get(prop_id)
    if prop:
        db.session.delete(prop)
        db.session.commit()
