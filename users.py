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
    all_users, all_usernames, all_ids = [], [], []

    def __init__(self, username: str, password: str, phone_number: str = None):
        """
        The __init__ method for assigning attributes
        """
        self.username, self.__password = username, password
        self.phone_number = phone_number
        self.user_id = User.uuid_gen(username)
        User.all_users.append(self)
        User.all_usernames.append(username)
        User.all_ids.append(self.user_id)

    def __str__(self):
        return f"Username: {self.username}\nPhone number: {self.phone_number}\nUser ID: {self.user_id}"

    def sign_in_validation(self, user_name, passwd):
        if user_name not in User.all_usernames:
            raise ValueError("Username not found! ")
        if (user_name == self.username) and (passwd == self.__password):
            print("Signing in Completed! ")
            return True
        print("Wrong Password! ")
        return False

    dictionary = {}

    @classmethod
    def signup(cls, user_name, passwd, ph_numb):
        """
        This function is for Signing up users.
        first user must enter username, then enter password
        and finally enter phone number
        """
        obj = cls(user_name, passwd, ph_numb)
        User.dictionary[user_name] = obj
        print("\nSignup Completed! ")

    def representation(self):
        print(self.__str__)

    @staticmethod
    def username_check(user_name: str) -> bool:
        """
        This static method actually for checking repetitious usernames
        """
        if user_name in User.all_usernames:
            return False
        return True

    def edit_user(self, usr_name=None, ph_numb=None):
        if usr_name is not None:
            self.username = usr_name
        if ph_numb is not None:
            self.phone_number = ph_numb

    def passwd_change(self, old_pass, new_pass, repeat_new_pass):
        if (old_pass != self.__password) or (new_pass != repeat_new_pass):
            raise ValueError("Invalid old Password of not mathc new passwords")
        self.__password = new_pass

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
        """
        Getter for password
        """
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


def main():
    """
    This is main function of our module
    """
    user1 = User("Matin", "12345678", phone_number="09197951537")
    user2 = User("Saman", "qwerty")
    user3 = User("Mehdi", "zxcvbnm")
    print(user1.username, user2.username, user3.username, sep="****")
    print(User.all_users)
    print(User.all_usernames)
    print(User.all_ids)


if __name__ == "__main__":
    main()
