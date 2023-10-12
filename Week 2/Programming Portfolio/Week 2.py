#Last week you wrote a program that printed out a cheery greeting including yourname. Take a copy of it, and modify it so that the user enters their name at the keyboard, and then receives a greeting.
name = input("Hello, what is your name?          ")
print("Hello " + name + ", Good to meet you!")
#Write a program that prompts a user to enter a temperature in Celsius, and then displays the corresponding temperature in Fahrenheit
celsius = float(input("Enter a temperature in Celsius:        "))
print(str(celsius) + "C is equivalent to " + str((celsius * 1.8) + 32) + "F")
#The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is usually 24 students, but this is sometimes varied to create groups of similar size. Write a program that prompts for the number of students and group size, and then displays how many groups will be needed and how many will be left over in a smaller group.
students = int(input("Number of students:      "))
groupsize = int(input("Required group size:          "))
fullgroup = (students//groupsize)
leftover = (students % groupsize)
if leftover == 1 and fullgroup == 1:
    print("There will be " + str(fullgroup) + " group with " + str(leftover)+" student in the leftover group")
elif leftover == 1:
    print("There will be " + str(fullgroup) + " groups with " + str(leftover)+" student in the leftover group")
elif groupsize == 1:
    print("There will be " + str(fullgroup) + " group with " + str(leftover)+" students in the leftover group")
else:
    print("There will be " + str(fullgroup) + " groups with " + str(leftover)+" students in the leftover group")
#A kindly teacher wishes to distribute a tub of sweets between her pupils. She will first count the sweets and then divide them according to how many pupils attend that day. Write a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left over.
sweets = int(input("Number of sweets:      "))
students = int(input("Number of students       "))
print("Each student will get "+ str(sweets // students) + " sweets each, and there will be " + str(sweets % students) + " sweets left over")