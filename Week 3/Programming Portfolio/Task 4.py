"""Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

badpassword = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
print("Set a password! It must be between 8 and 12 characters long")
password = input("Enter a password:         ")
if password == badpassword():
    print("Password cannot be this commonly used phrase")
    quit()
if len(password) < 8 or len(password) > 12:
    print("Password must have between 8 and 12 characters")
    quit()

password1 = input("Confirm your password:         ")
if password == password1:
    print("Password set")
else:
    print("Sorry, passwords did not match")