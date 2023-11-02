"""Write some code that uses the extend() method to add the next three square
values, starting at 121 (11 x 11), to the end of the squares list."""
squares = [4, 9, 16, 25]
squares.append(36)
squares.append(49)
squares.append(64)
squares.append(81)
squares.extend([121, 144, 169])
print(squares)