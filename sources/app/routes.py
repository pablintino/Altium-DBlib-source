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


from app import api
from rest_layer.component_list_resource import ComponentListResource
from rest_layer.component_resource import ComponentResource
from rest_layer.footprint_component_reference_resource import FootprintComponentReferenceResource
from rest_layer.footprint_data_resource import FootprintDataResource
from rest_layer.footprint_element_component_reference_resource import FootprintElementComponentReferenceResource
from rest_layer.footprint_list_resource import FootprintListResource
from rest_layer.footprint_resource import FootprintResource
from rest_layer.inventory.inventory_item_location_resource import InventoryItemLocationResource
from rest_layer.inventory.inventory_item_property_element_resource import InventoryItemPropertyElementResource
from rest_layer.inventory.inventory_item_property_list_resource import InventoryItemPropertyListResource
from rest_layer.inventory.inventory_item_resource import InventoryItemResource
from rest_layer.inventory.inventory_item_stock_location_resource import InventoryItemStockLocationResource
from rest_layer.inventory.inventory_location_list_resource import InventoryLocationListResource
from rest_layer.inventory.inventory_location_resource import InventoryLocationResource
from rest_layer.inventory.inventory_stocks_mass_update_resource import InventoryStocksMassUpdateResource
from rest_layer.metadata_api import MetadataResource
from rest_layer.symbol_component_reference_resource import SymbolComponentReferenceResource
from rest_layer.symbol_data_resource import SymbolDataResource
from rest_layer.symbol_list_resource import SymbolListResource
from rest_layer.symbol_resource import SymbolResource


api.add_resource(MetadataResource, '/metadata')
api.add_resource(ComponentListResource, '/components')
api.add_resource(ComponentResource, '/components/<int:id>')
api.add_resource(SymbolComponentReferenceResource, '/components/<int:id>/symbol')
api.add_resource(FootprintComponentReferenceResource, '/components/<int:id>/footprints')
api.add_resource(FootprintElementComponentReferenceResource, '/components/<int:id>/footprints/<int:id_f>')
api.add_resource(SymbolListResource, '/symbols')
api.add_resource(SymbolResource, '/symbols/<int:id>')
api.add_resource(SymbolDataResource, '/symbols/<int:id>/data')
api.add_resource(FootprintListResource, '/footprints')
api.add_resource(FootprintResource, '/footprints/<int:id>')
api.add_resource(FootprintDataResource, '/footprints/<int:id>/data')
api.add_resource(InventoryItemResource, '/inventory/items/<int:id>')
api.add_resource(InventoryItemLocationResource, '/inventory/items/<int:id>/locations')
api.add_resource(InventoryItemPropertyListResource, '/inventory/items/<int:id>/properties')
api.add_resource(InventoryItemPropertyElementResource, '/inventory/items/<int:id>/properties/<int:prop_id>')
api.add_resource(InventoryItemStockLocationResource, '/inventory/items/<int:id>/locations/<int:id_loc>/stock')
api.add_resource(InventoryLocationListResource, '/inventory/locations')
api.add_resource(InventoryLocationResource, '/inventory/locations/<int:id>')
api.add_resource(InventoryStocksMassUpdateResource, '/inventory/stocks/updates')
