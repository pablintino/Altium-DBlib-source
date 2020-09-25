from app import db


class InventoryIdentificableItemModel(db.Model):
    __abstract__ = True
    __id_prefix__ = 'ITEM'

    def get_id_prefix(self):
        return self.__id_prefix__
