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


class MassStockMovement:

    def __init__(self, reason, comment, movements):
        self.reason = reason
        self.comment = comment
        self.movements = movements


class SingleStockMovement:

    def __init__(self, quantity, item_dici=None, item_id=None, location_dici=None, location_id=None):
        self.item_dici = item_dici
        self.item_id = item_id
        self.location_dici = location_dici
        self.location_id = location_id
        self.quantity = quantity


class InventoryMassStockMovementResult:

    def __init__(self, stock_levels):
        self.stock_levels = stock_levels


class InventoryItemStockStatus:

    def __init__(self, stock_level, item_dici, location_dici):
        self.stock_level = stock_level
        self.item_dici = item_dici
        self.location_dici = location_dici
