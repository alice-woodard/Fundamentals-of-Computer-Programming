"""Try writing an if statement similar to the last example that includes an extra elif
clause to check ages between 30-40. Print a suitable message in the associated code block."""
age = int(input("What is your age?           "))
if (18 <= age <= 30):
    print("You are still young!")
elif (30< age <= 40):
    print("You are middle aged")