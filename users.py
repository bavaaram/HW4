# 1 /usr/bin/python3

import uuid


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

    all_users, all_usernames, all_ids = [], [], []

    def __init__(self, username: str, password: str, phone_number: str = None):
        """
        The __init__ method for assigning attributes
        """
        self.username, self.password = username, password
        self.phone_number = phone_number
        self.user_id = User.uuid_gen(username)
        User.all_users.append(self)
        User.all_usernames.append(username)
        User.all_ids.append(self.user_id)

    def __str__(self):
        """
        This is a __str__ magic method for/
        returning user Information as a string
        """
        return f"\nUser Information:\n\tUsername: {self.username}\n\tPhone Number: {self.phone_number}\n\tUser ID: {self.user_id}"
    
    def sign_in_check(self, user_name, passwd):
        if (user_name == self.username) and (passwd == self.password):
            print("Signing In Completed! ")
        else:
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
                cls_obj = cls.dictionary[user_name]
        cls_obj.sign_in_check(user_name, passwd)

    dictionary = {}

    @classmethod
    def signup(cls, user_name: str, passwd: str, ph_numb: str = None):
        """
        This function is for Signing up users.
        first user must enter username, then enter password
        and finally enter phone number
        """
        obj = cls(user_name, passwd, ph_numb)
        User.dictionary[user_name] = obj
        print("\nSignup Completed! ")

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

    def edit_user(self, original_username: str, usr_name: str = None, ph_numb: str = None):
        """
        This method is used for username and/
        phone number editing
        if given username or phone number in not None/
        , assigning given username and phone number/
        to this instance Attributes
        """
        if usr_name in User.all_usernames:
            raise RepUserError("Username already Taken! ")
        if usr_name is not None:
            self.username = usr_name
        if ph_numb is not None:
            self.phone_number = ph_numb

    def passwd_change(self, old_pass: str, new_pass: str, repeat_new_pass: str):
        """
        This function is for password changing.
        if entered old password in not match to original password/
        or new password and Repeat it not match together/
        raise an error.
        """
        if (old_pass != self.password) or (new_pass != repeat_new_pass):
            raise TwoPasswordError("Invalid Password or unmatch new passwords")
        self.password = new_pass

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
