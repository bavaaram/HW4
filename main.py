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

        while 1:
            print("\n************** - User Dashboard - **************\n")
            stat = input("Stat (1(Show User Information) - 2(Edit) - 3(Password Change) - 4(Back to Main Menu)):   ")

            if stat == "1":
                user_object = User.representation()

            elif stat == "2":
                print("\n********** ^ Edit User information mode ^ **********\n")
                print("if you dont want to change any item, just leave it and press Enter.\n")
                try:
                    new_username = input("Enter New Username: ")
                    new_phone_number = input("Enter New Phone Number")
                    user_object.edit_user(username, new_username, new_phone_number)
                except RepUserError:
                    print("Username already Taken! ")
                    print("\nUser Information has been Updated! ")

            elif stat == "3":
                print("\n********** ^ Password Change ^ **********\n")
                try:
                    old_pass = input("Enter Old Password: ")
                    new_pass = input("Enter New Password: ")
                    rep_new_pass = input("Enter New Password again: ")
                    user_object.passwd_change(old_pass, new_pass, rep_new_pass)
                except ShortPasswordError:
                    print("Too short password! ")
                except TwoPasswordError:
                    print("Two new passwords are not matched! ")
                print("\nYour Password has been changed! ")

            elif stat == "4":
                print("\nExiting User Panel...")
                break

            else:
                print("\nInvalid State! ")
                continue

    else:
        print("\nInvalid State! ")
        continue
