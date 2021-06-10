"""
A calculator than can compute the area of a given shape, as selected by the user. The calculator will be able to determine the area of the following shapes:

Circle
Triangle
The program should do the following:

Prompt the user to select a shape
Depending on the shape the user selects, calculate the area of that shape
Print the area of that shape to the user
Let's begin!
"""

from math import pi

print "Calculator is starting up..."
print "What shape would you like to calculate the area for?"

option = raw_input("Enter C for Circle or T for Triangle:  ")

if option == "C":
  radius = float(raw_input("Enter radius: "))
  area = pi * radius**2
  print "Area: %f" % area
elif option == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "Area: %f" % area
else:
  print "Error!  Invalid shape."

print "Exiting..."
  
