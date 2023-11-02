"""Write some code that makes a copy of the colours using the copy() method.
Then make some changes to the original list. Print the contents of the copied list to ensure
these changes have not affected the copy."""
colours = ["red", "green", "yellow", "blue", "red"]
newcolours = colours.copy()
colours.append("indigo")
print(newcolours)
print(colours)