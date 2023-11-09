"""Amend your previous solution so that if any value within the list is found to be over
100 then the loop should break immediately."""
numbers = [10, 20 , 30, 90, 200, 30, 22, 11]
g = 0
for n in numbers:
    if n >= 100:
        break
    else:
         g = g + n
         print (g)