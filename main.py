#! /usr/bin/python3

from users import User,UserError, PasswordError, TwoPasswordError, ShortPasswordError, RepUserError


while 1:
    try:
        stat = int(input("Stat (0(Exit) - 1(Sign Up) - 2(Sign In)):   "))
    except NameError:
        print("Invalid State! ")
        continue

    if stat == "0":
        print("Exiting the User Management Panel... ")
        break

    elif stat == "1":
        try:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            phone_number = input("Enter Phone number(Optional): ")
            User.signup(username, password, phone_number)
        except UserError:
            print("Username Already Taken! ")
        except ShortPasswordError:
            print("Too Short Password! ")

    elif stat == "2":
        print("\n************** - Login form - **************\n")
        try:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            User.sign_in_validation(username, password)
            user_object = User.dictionary[username]
        except UserError:
            print("Username not Found! ")
        except PasswordError:
            print("Wrong Password! ")




