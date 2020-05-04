"""
Homework Problem # 1.7
Description: Writing two separate formulas to estimate pi 
"""

# Create two formulas to show the results of PI

# Set a varibale for the shorter version of the PI formula
# Use round to narrow the decimal point to six places
PI1 = round(4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11), 6)
# Set a variable for the second version of PI
PI2 = round(4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15), 6)


print("A short approximation of PI is ", PI1)
print("An extended approximation of PI is", PI2)



