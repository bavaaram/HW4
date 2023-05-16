#! /usr/bin/python3
from users import User

while 1:
    try:
        stat = int(input())
    except NameError:
        print("Invalid State! ")
        continue

    if stat not in [0, 1, 2, 3, 4]:
        print("Invalid Stat! ")
        continue
    if stat == 0:
        break
    if stat == 1:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        phone_number = input("Enter Phone number(Optional): ")
        User.signup(username, password, phone_number)
    if stat == 2:
        print("************** - Login form - **************")
        username = input("Enter Username: ")
