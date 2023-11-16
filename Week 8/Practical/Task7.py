"""Use a text editor to create a file called info.txt and enter the text shown below.
Once the file has been created and saved, write a small program that:
1. Opens the file,
2. reads and prints the contents,
3. closes the file."""
f = open("info.txt")
f.read()
f.close()