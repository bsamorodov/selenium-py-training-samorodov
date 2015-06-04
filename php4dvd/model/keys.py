class Keys(object):

    def __init__(self, keys=None):
        self.keys = keys

    @classmethod
    def TestFilm(cls):
        return cls(keys="Test film")
