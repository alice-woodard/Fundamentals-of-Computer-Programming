# The Head of Computing at the University of Poppleton is tasked with
# dividing a group of students into lab groups.
# A lab group is 24 students, since this is the number of PCs in a lab.
# Write a program that calculates how many groups are needed for the following number of students:
# 113, 175, 12. Display how many full groups there will be,
# and how many students will be in the smaller "left over" group.
fullgroup = (113//24)
leftover = (113 % 24)
print("Full groups: " + str(fullgroup) + " Students in Left Over group: " + str(leftover))
fullgroup = (175//24)
leftover = (175 % 24)
print("Full groups: " + str(fullgroup) + " Students in Left Over group: " + str(leftover))
fullgroup = (12//24)
leftover = (12 % 24)
print("Full groups: " + str(fullgroup) + " Students in Left Over group: " + str(leftover))