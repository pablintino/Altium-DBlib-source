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
from models.internal.internal_inventory_models import MassStockMovement, SingleStockMovement
from models.inventory.inventory_item_model import InventoryItemModel
from models.inventory.inventory_item_property import InventoryItemPropertyModel
from models.inventory.inventory_location import InventoryLocationModel


class InventoryItemDto:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.mpn = kwargs.get('mpn', '')
        self.manufacturer = kwargs.get('manufacturer', '')
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.last_buy_price = kwargs.get('last_buy_price', '')
        self.dici = kwargs.get('dici', '')
        self.component = kwargs.get('component', None)

    @staticmethod
    def to_model(data):
        return InventoryItemModel(
            id=data.id,
            mpn=data.mpn,
            manufacturer=data.manufacturer,
            name=data.name,
            description=data.description,
            last_buy_price=data.last_buy_price,
            dici=data.dici)

    @staticmethod
    def from_model(data, component_dto=None):
        return InventoryItemDto(
            id=data.id,
            mpn=data.mpn,
            manufacturer=data.manufacturer,
            name=data.name,
            description=data.description,
            last_buy_price=data.last_buy_price,
            dici=data.dici,
            component=component_dto)


class InventoryLocationDto:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.dici = kwargs.get('dici', '')

    @staticmethod
    def to_model(data):
        return InventoryLocationModel(
            id=data.id,
            name=data.name,
            description=data.description,
            dici=data.dici)

    @staticmethod
    def from_model(data):
        return InventoryLocationModel(
            id=data.id,
            name=data.name,
            description=data.description,
            dici=data.dici)


class InventoryItemLocationRelationDto:

    def __init__(self, location_ids):
        self.location_ids = location_ids

    @staticmethod
    def from_model(location_ids):
        return InventoryItemLocationRelationDto(location_ids=location_ids)


class InventoryItemLocationStockDto:

    def __init__(self, id=None, actual_stock=None, stock_min_level=None, stock_notify_min_level=None):
        self.id = id
        self.actual_stock = actual_stock
        self.stock_min_level = stock_min_level
        self.stock_notify_min_level = stock_notify_min_level

    @staticmethod
    def from_model(data):
        return InventoryItemLocationStockDto(
            id=data.id,
            actual_stock=data.actual_stock,
            stock_min_level=data.stock_min_level,
            stock_notify_min_level=data.stock_notify_min_level,
        )


class InventorySingleStockMovementDto:
    def __init__(self, quantity, location_dici=None, location_id=None, item_dici=None, item_id=None):
        self.location_dici = location_dici
        self.location_id = location_id
        self.item_id = item_id
        self.item_dici = item_dici
        self.quantity = quantity

    @staticmethod
    def to_model(data):
        return SingleStockMovement(
            item_dici=data.item_dici,
            item_id=data.item_id,
            location_id=data.location_id,
            location_dici=data.location_dici,
            quantity=data.quantity)


class InventoryMassStockMovementDto:
    def __init__(self, reason, comment=None, movements=None):
        self.reason = reason
        self.comment = comment
        self.movements = movements

    @staticmethod
    def to_model(data):
        return MassStockMovement(
            reason=data.reason,
            comment=data.comment,
            movements=[InventorySingleStockMovementDto.to_model(ent) for ent in data.movements])


class InventoryItemStockStatusDto:
    def __init__(self, stock_level, item_dici, location_dici):
        self.stock_level = stock_level
        self.item_dici = item_dici
        self.location_dici = location_dici

    @staticmethod
    def from_model(data):
        return InventoryItemStockStatusDto(
            stock_level=data.stock_level,
            item_dici=data.item_dici,
            location_dici=data.location_dici
        )


class InventoryMassStockMovementResultDto:

    def __init__(self, stock_levels):
        self.stock_levels = stock_levels

    @staticmethod
    def from_model(data):
        return InventoryMassStockMovementResultDto(
            stock_levels=[InventoryItemStockStatusDto.from_model(ent) for ent in data.stock_levels])


class InventoryItemPropertyDto:

    def __init__(self, name, id=None, value=None):
        self.id = id
        self.name = name
        self.value = value

    @staticmethod
    def to_model(data):
        model = InventoryItemPropertyModel(id=data.id, property_name=data.name)
        model.set_value(data.value)
        return model

    @staticmethod
    def from_model(data):
        return InventoryItemPropertyDto(id=data.id, name=data.property_name, value=data.get_value())


class InventoryItemPropertyUpdateDto:

    def __init__(self, value=None):
        self.value = value


class InventoryItemPropertiesDto:

    def __init__(self, properties=None):
        self.properties = properties

    @staticmethod
    def from_model(data):
        return InventoryItemPropertiesDto(properties=[InventoryItemPropertyDto.from_model(prop) for prop in data])