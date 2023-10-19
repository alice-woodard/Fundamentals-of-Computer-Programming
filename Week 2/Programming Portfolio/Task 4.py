"""A kindly teacher wishes to distribute a tub of sweets between her pupils.
She will first count the sweets and then divide them according to how many pupils attend that day.
Write a program that will tell the teacher how many sweets to give to each pupil,
and how many she will have left over."""
sweets = int(input("Number of sweets:      "))
students = int(input("Number of students       "))
print("Each student will get "+ str(sweets // students) + " sweets each, and there will be " + str(sweets % students) + " sweets left over")