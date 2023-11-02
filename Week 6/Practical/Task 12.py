"""Improve your previous solution so that the list is sorted correctly, ignoring the case
used to write the names. To achieve this you will have to include a key argument in the form
of a lambda expression that returns each string as uppercase letters only. Hint: you can use
the str.upper() method to convert a name to uppercase letters."""
names = [ "Eric", "anna", "Sophie", "sam" ]
names.sort(key=lambda n : str.upper(n))
print(names)