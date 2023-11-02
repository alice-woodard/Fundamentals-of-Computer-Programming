"""Use sequence unpacking to extract the values you stored within the address tuple
earlier. Unpack the tuple into variables named house_num, street and postcode."""
address = ("Flat 13", "Warehouse", "Kirkstall Brewery", "Broad Lane", "Kirkstall", "LEEDS", "LS53RX")
postcode = address[-1]
house_num = address[0]
street = address[3]
print(postcode, house_num, street)