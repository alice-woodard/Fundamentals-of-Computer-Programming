""" Write some code that uses the remove() method to remove the value 3 from the
squares list. Notice how an error is generated since the given value was not present."""
squares = [4, 9, 16, 25]
squares.append(36)
squares.append(49)
squares.append(64)
squares.append(81)
squares.extend([121, 144, 169])
squares.insert(0,2)
squares.remove(49)
squares.remove(3)
print(squares)