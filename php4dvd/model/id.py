class Id(object):

    def __init__(self,  name=None):
        self.name = name

    @classmethod
    def Q(cls):
        return cls(name="q")

    @classmethod
    def Results(cls):
        return cls(name="results")

    @classmethod
    def UpdateForm(cls):
        return cls(name="updateform")
