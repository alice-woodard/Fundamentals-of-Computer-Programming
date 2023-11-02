"""TASK: Write some code that uses the pop() method to remove and display the first value of
the squares list. Print the list afterwards to ensure the value has been removed."""
squares = [4, 9, 16, 25]
squares.append(36)
squares.append(49)
squares.append(64)
squares.append(81)
squares.extend([121, 144, 169])
squares.insert(0,2)
squares.remove(49)
a = squares.pop(10)
print(a)
b = squares.pop(0)
print(b)
print(squares)
