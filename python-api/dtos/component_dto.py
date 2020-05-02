
class ComponentDto:

    def __init__(self, id, type, mpn, manufacturer, value, package, description, comment):
        self.id = id
        self.type = type
        self.mpn = mpn
        self.manufacturer = manufacturer
        self.value = value
        self.package = package
        self.description = description
        self.comment = comment

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
