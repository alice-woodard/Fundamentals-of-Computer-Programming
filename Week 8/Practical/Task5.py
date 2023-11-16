"""Write some code that uses the str.format() method to display the area of a circle
with a radius specified by the variable r. Use a keyword replacement field called area to
identify the calculated area and refer to this when passing the value to the str.format()
method. The output should look like the following, in the case where r is set to 52."""
import math
r=52
area = math.pi * r * r
print("A circle with the radius '{r}' has an area of {area}".format(r = r,area = area))