from enum import Enum


class StorableLibraryResourceType(Enum):
    FOOTPRINT = 'footprint'
    SYMBOL = 'symbol'


class StorageStatus(Enum):
    NOT_STORED = 1
    STORING = 2
    STORED = 3
    STORAGE_FAILED = 4
