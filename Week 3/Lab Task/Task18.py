"""Amend your previous solution once again, so that the message “all numbers
processed” is printed when the loop completes, but only if all values were less or equal to
100 (i.e. the loop did not break early)"""
numbers = [10, 20 , 30, 90, 200, 30, 22, 11]
g = 0
for n in numbers:
    if n >= 100:
        break
    elif n <= 100:
         g = g + n
         print (g)
    else:
        print("All numbers processed")
