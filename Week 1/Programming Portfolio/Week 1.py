#Write a program that prints a cheery message (such as "Hello World") on the screen.
print("Hello World")
#Make a copy of the previous program, and modify it so that it displays your name.
print("Hello Alice")
#Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that converts this value in Celsius to the equivalent temperature in Fahrenheit, and then displays both.
print((38.4 * 1.8) + 32)
#In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014 times, was not out 162 times, and scored 48426 runs. Write a program to calculate and display Boycott's batting average.
print(48426 / (1014 - 162))
#The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is 24 students, since this is the number of PCs in a lab. Write a program that calculates how many groups are needed for the following number of students: 113, 175, 12. Display how many full groups there will be, and how many students will be in the smaller "left over" group.
fullgroup = (113//24)
leftover = (113 % 24)
print("Full groups: " + str(fullgroup) + " Students in Left Over group: " + str(leftover))
fullgroup = (175//24)
leftover = (175 % 24)
print("Full groups: " + str(fullgroup) + " Students in Left Over group: " + str(leftover))
fullgroup = (12//24)
leftover = (12 % 24)
print("Full groups: " + str(fullgroup) + " Students in Left Over group: " + str(leftover))
