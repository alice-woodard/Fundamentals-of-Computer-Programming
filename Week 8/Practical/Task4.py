"""Write a print() statement that displays the name and age values, with a column
width of 20 for each, both right aligned, and with the age being shown to two decimal
places. The fill character should be a dollar symbol $."""
name = "Alice"
age = 18
print(f"{name:$>20} - {age:$>20}")