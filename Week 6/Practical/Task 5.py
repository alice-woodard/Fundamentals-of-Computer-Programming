"""Write some code that uses the insert() method to insert the value 2, to the very
beginning of the squares list."""
squares = [4, 9, 16, 25]
squares.append(36)
squares.append(49)
squares.append(64)
squares.append(81)
squares.extend([121, 144, 169])
squares.insert(0,2)
print(squares)