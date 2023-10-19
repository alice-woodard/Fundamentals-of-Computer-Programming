# The Head of Computing at the University of Poppleton is tasked with dividing a group of students
# into lab groups. A lab group is usually 24 students, but this is sometimes varied to create groups of
# similar size. Write a program that prompts for the number of students and group size, and then displays how
# many groups will be needed and how many will be left over in a smaller group.
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