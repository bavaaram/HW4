#1 /usr/bin/python3

class User:
    all = []

    def __init__(self, username: str, password: str, phone_number: str=None):
        """
        The __init__ method for assigning attributes
        """
        self.username, self.__password = username, password
        self.phone_number = phone_number
        User.all.append(self)


