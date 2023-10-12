# Write a program that prompts a user to enter a temperature in Celsius,
# and then displays the corresponding temperature in Fahrenheit
celsius = float(input("Enter a temperature in Celsius:        "))
print(str(celsius) + "C is equivalent to " + str((celsius * 1.8) + 32) + "F")