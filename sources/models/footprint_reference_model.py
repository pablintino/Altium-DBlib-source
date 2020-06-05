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


from sqlalchemy import Column, String, Integer, Enum

from .internal.internal_models import StorageStatus
from .join_tables import component_footprint_asc_table
from sqlalchemy.orm import relationship
from app import db


class FootprintReference(db.Model):
    __tablename__ = "footprint_ref"
    id = Column(Integer, primary_key=True)
    footprint_path = Column(String(300))
    footprint_ref = Column(String(150))
    description = Column(String(200))
    storage_status = Column(Enum(StorageStatus))

    # relationships
    components_f = relationship("ComponentModel",
                                secondary=component_footprint_asc_table,
                                back_populates="footprint_refs",
                                lazy=True)

    def __repr__(self):
        return "FootprintReference %s %s" % (
            self.footprint_path,
            self.footprint_ref,
        )
