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


from models import LibraryReference


class SymbolDto:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.path = kwargs.get('path', '')
        self.reference = kwargs.get('reference', '')
        self.encoded_data = kwargs.get('encoded_data', '')
        self.description = kwargs.get('description', '')

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    @staticmethod
    def to_model(data):
        return LibraryReference(
            symbol_path=data.path,
            symbol_ref=data.reference,
            description=data.description)

    @staticmethod
    def from_model(data, encoded_symbol):
        return SymbolDto(
            id=data.id,
            path=data.symbol_path,
            reference=data.symbol_ref,
            description=data.description,
            encoded_data=encoded_symbol)


class SymbolComponentReferenceDto:

    def __init__(self, **kwargs):
        self.symbol_id = kwargs.get('symbol_id', None)

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
