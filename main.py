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




