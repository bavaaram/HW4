#1 /usr/bin/python3

import uuid
import hashlib
import getpass

class User:
    """
    This class is use for modeling users and some functionality/
    like username, password, a unique identifier and phone number./
    this class recieves informations from user and processing them./
    password must longer than 4 characters/
    username must be unique and repetitious usernames not accepted/
    also user can enter his/her phone number and if phone number not entered,
     it assuming to None
    """
    all, all_usernames = [], []

    def __init__(self, username: str, password: str, phone_number: str = None):
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

    @property
    def username(self):
        """
        Getter for Username
        """
        return self.username

    @username.setter
    def username(self, user_value):
        if not User.username_check(user_value):
            raise ValueError("Username is already taken! ")

    @staticmethod
    def password_check(passwd):
        """
        This function actually check the password and if its length smaller
        than 4, an ValueError raised with the too short massage
        """
        if len(passwd) < 4:
            return False
        return True

    @property
    def __password(self):
        return self.__password

    @__password.setter
    def __password(self, passwd_value):
        if not User.password_check(passwd_value):
            raise ValueError("Too short Password! ")

    @staticmethod
    def uuid_gen(name):
        """
        This function generate a universal unique identifier with uuid5
        and use MD5 Hash algorithm
        """
        x_uuid = uuid.uuid1()
        return uuid.uuid5(x_uuid, name)

