# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again.
# If the two passwords entered are the same the program should say "Password Set" or similar,
# otherwise it should report an error.
print("Set a password! It must be between 8 and 12 characters long")
password = input("Enter a password:         ")
print("hello")
password1 = input("Confirm your password:         ")
if password == password1:
    print("Password set")
else:
    print("Sorry, passwords did not match")