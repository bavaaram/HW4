# 1 /usr/bin/python3

import uuid
import hashlib
import os

class ShortPasswordError(Exception):
    """
    I use this Error when Short Password has been Entered.
    """


class PasswordError(Exception):
    """
    I use this Error when Wrong Password has been Entered.
    """


class UserError(Exception):
    """
    I use this Error When Wrong Username has been Entered.
    """


class RepUserError(Exception):
    """
    I use this Error When Repetitious Username has been Entered.
    """


class TwoPasswordError(Exception):
    """
    I use this Error When two New Passwords are not Match.
    """


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

    @staticmethod
    def hashing(passwd: str, salt: str) -> str:
        """
        this is a static method that generates hash from a password 
        and unique salt for each user
        """
        hashed_pass = hashlib.pbkdf2_hmac("sha256", passwd.encode("utf-8"), salt, 100000)
        return hashed_pass

    all_users, all_usernames = [], []
    all_ids, all_hashes, all_salts = [], [], []

    def __init__(self, username: str, password: str, phone_number: str = None):
        """
        The __init__ method for assigning attributes
        """
        self.username, self.password = username, password   # assigning username and regular password
        self.user_id = User.uuid_gen(username)
        self.salt = os.urandom(32)   # Generate a unique slat for each user
        self.phone_number = phone_number
        self.password = User.hashing(password, self.salt)   # Generating hash for each password
        User.all_users.append(self)   # storing each user object in a list
        User.all_usernames.append(username)   # storing each username in a list
        User.all_ids.append(self.user_id)   # storing each user ID in a list
        User.all_hashes.append(self.password)   # storing each hashed passwords in a list

    def __str__(self):
        """
        This is a __str__ magic method for/
        returning user Information as a string
        """
        return f"\nUser Information:\n\tUsername: {self.username}\n\tPhone Number: {self.phone_number}\n\tUser ID: {self.user_id}"

    def password_login_check(self, passwd):
        """
        this method is used for password check
        if entered password is not equal to/
        real password, an error raised
        """
        new_key = User.hashing(passwd, self.salt)   # generating hash from enterd password for login
        if not new_key == self.password:   # if hashed entered password is not equal to stored hashed password from sign up, an error has been raised
            raise PasswordError("Wrong Password! ")

    @classmethod
    def sign_in_validation(cls, user_name: str, passwd: str) -> bool:
        """
        This method is for sign in validation/
        and give username and password/
        if given username not in usernames list/
        rasing an Error that says Username not found
        and if entered username and password is/
        match to self.username and self.password
        printing sign in complete,/
        else if entered password is not match/
        print wrong password error.
        """
        if user_name not in cls.all_usernames:
            raise UserError("Username not found! ")
        for usr in cls.all_usernames:
            if user_name == usr:
                cls_obj = User.get_obj(user_name)
        cls_obj.password_login_check(passwd)
        return cls_obj

    dictionary = {}

    @classmethod
    def signup(cls, user_name: str, passwd: str, ph_numb: str = None):
        """
        This function is for Signing up users.
        first user must enter username, then enter password
        and finally enter phone number
        """
        obj = cls(user_name, passwd, ph_numb)
        User.dictionary[obj] = user_name   # store user objects as key and usernames as value in a dictionary

    @staticmethod
    def get_obj(user_name: str):
        """
        This method is used for getting every user object with its username.
        """
        for obj in User.all_users:
            if obj.username == user_name:
                return obj

    def representation(self):
        """
        This method actually print User Information/
        with __str__ magic method
        """
        print(self)

    @staticmethod
    def username_check(user_name: str) -> bool:
        """
        This static method actually for checking repetitious usernames
        """
        if user_name in User.all_usernames:
            return False
        return True

    def edit_user(self, usr_name: str = None, ph_numb: str = None):
        """
        This method is used for username and/
        phone number editing
        if given username or phone number in not None/
        , assigning given username and phone number/
        to this instance Attributes
        """
        if usr_name in User.all_usernames:
            raise RepUserError("Username already Taken! ")
        if usr_name != "":
            User.all_usernames.remove(self.username) # remove former username from all usernames list
            self.username = usr_name # assigning new username to desired user object
            User.all_usernames.append(self.username) # add new username to all usernames list
            User.dictionary[self] = usr_name # change the value of the user object to new username
        if ph_numb != "":
            self.phone_number = ph_numb # Assign new phone number to user object

    def passwd_change(self, old_pass: str, new_pass: str, rep_new_pass: str):
        """
        This function is for password changing.
        if entered old password in not match to original password/
        or new password and Repeat it not match together/
        raise an error.
        """
        old_key = User.hashing(old_pass, self.salt) # generate a hash from entered old password
        new_key = User.hashing(new_pass, self.salt) # generate a hsah from entered new password
        rep_new_key = User.hashing(rep_new_pass, self.salt) # generate a hash from rep_new_password
        if old_key != self.password: # If entered old password hash is not equal to original hash password, an error raised
            raise PasswordError("Wrong original Password! ")
        if new_key != rep_new_key: # If new entered password hash is not equal to rep_new_password hash, an error raised
            raise TwoPasswordError("Unmatched new passwords")
        elif len(new_pass) < 4:
            raise ShortPasswordError("Too Short New Passwords! ")
        User.all_hashes.remove(self.password) # if password changing operation is completed, remove old password hash from all_hashes list
        self.password = new_key # Assigning new password hash to user object password Attribute
        User.all_hashes.append(self.password) # Ad this new hash to all_hashes list

    @property
    def username(self):
        """
        Getter for Username
        """
        return self._username

    @username.setter
    def username(self, user_value):
        if not User.username_check(user_value):
            raise RepUserError("Username is already taken! ")
        self._username = user_value

    @staticmethod
    def password_check(passwd: str) -> bool:
        """
        This function actually check the password and if its length smaller
        than 4, an ValueError raised with the too short massage
        """
        if len(passwd) < 4:
            return False
        return True

    @property
    def password(self):
        """
        Getter for password
        """
        return self.__password

    @password.setter
    def password(self, passwd_value):
        if not User.password_check(passwd_value):
            raise ShortPasswordError("Too short Password! ")
        self.__password = passwd_value

    @staticmethod
    def uuid_gen(name: str) -> str:
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
