"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: 25 January 2020
Homwork Problem # 1.9
Description: Calculating the Area and Perimeter of a rectangle 
"""


# Set the width variable
width = 4.5
# Set the height varaible
height = 7.9
# Given: Area = width * height. Set the formual for the area
area = round(width * height, 2) # without this round this extends 
# Given: Perimeter of rectangle = 2 * (width + height) 
perimeter = 2 * (width + height)

print("The area of a rectangle with a width 4.5 and height of 7.9 is", area)
print("Its perimeter is equal to", perimeter)