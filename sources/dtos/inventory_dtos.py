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


from models.inventory.inventory_item_model import InventoryItemModel
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
    def from_model(data):
        return InventoryItemDto(
            id=data.id,
            mpn=data.mpn,
            manufacturer=data.manufacturer,
            name=data.name,
            description=data.description,
            last_buy_price=data.last_buy_price,
            dici=data.dici)


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
