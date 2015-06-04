Class Names(object):

    def __init__(self, name=None):
        self.name = name

    @classmethod
    def Name(cls):
        return cls(name="name")

    @classmethod
    def Year(cls):
        return cls(name="year")
