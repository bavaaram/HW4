#1 /usr/bin/python3

class User:
    all, all_usernames = [], []

    def __init__(self, username: str, password: str, phone_number: str=None):
        """
        The __init__ method for assigning attributes
        """
        self.username, self.__password = username, password
        self.phone_number = phone_number
        User.all.append(self)
        
    @staticmethod
    def username_check(user_name: str) -> bool:
        """
        This static method actually for checking repetitious usernames
        """
        if user_name in User.all_usernames:
            return False
        return True
