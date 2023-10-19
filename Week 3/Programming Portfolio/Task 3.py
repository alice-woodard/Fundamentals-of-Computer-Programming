"""Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long"""
print("Set a password! It must be between 8 and 12 characters long")
password = input("Enter a password:         ")
if len(password) < 8 or len(password) > 12:
    print("Password must have between 8 and 12 characters")
    quit()
password1 = input("Confirm your password:         ")
if password == password1:
    print("Password set")
else:
    print("Sorry, passwords did not match")