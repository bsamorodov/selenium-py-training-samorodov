class User(object):

    def __init__(self,  username=None, passaword=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def Admin(cls):
        return cls(username="admin", password="admin")
