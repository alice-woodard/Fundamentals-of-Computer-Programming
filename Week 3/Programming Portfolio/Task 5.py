"""Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time"""
check = True
while check == True:
    badpassword = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    print("Set a password! It must be between 8 and 12 characters long")
    password = input("Enter a password:         ")
    for n in badpassword:
        print(n)
        if password == n:
            print("Password cannot be this commonly used phrase")
            check = True
        if len(password) < 8 or len(password) > 12:
            print("Password must have between 8 and 12 characters")
            check = True
        else:
            check = False

password1 = input("Confirm your password:         ")
if password == password1:
    print("Password set")
    check = False
else:
    print("Sorry, passwords did not match")
    check = True
