""" Write some code that calls the print() function to output the contents of the
address tuple you created earlier. Ensure you use the ‘*’ prefix so that the elements are
extracted before being passed to the function. Compare this with a version of the same code
that calls the print() function without using the ‘*’ prefix,"""
address = ("Flat 13", "Warehouse", "Kirkstall Brewery", "Broad Lane", "Kirkstall", "LEEDS", "LS53RX")
print(*address)