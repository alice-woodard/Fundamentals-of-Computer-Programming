""" Convert the f-string based statement below into an equivalent that uses the
str.format() method to generate the same output."""
name = "Alice"
age = 18
print(f"{name:@^15} - {age:#^10}")
print("{i:@^15} - {o:#^10}".format(i = name, o=age))