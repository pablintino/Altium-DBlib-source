from json import JSONEncoder


class DtoEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class JsonizableBaseClass:

    def to_json(self):
        return DtoEncoder().encode(self)
