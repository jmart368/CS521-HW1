"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: 25 January 2020
Homwork Problem # 1.11
Description: Population projection from US Census Bureau where present
population is 312,032,486
"""

# set variable for current population
total_population = 312032486

# set variable for seconds in year
# seconds per minute * minutes per hour * hours per days * days per year
seconds = 60 * 60 * 24 * 365

# set variable in seconds for births per year for every 7 seconds
# use // to remove decimals
births = seconds / 7 

# set variable in seconds for deaths per year for every 13 seconds
deaths = -(seconds / 13) 

# set variable in seconds for immigrants per year for every 45 seconds
immigrants = 31536000 / 45 

# set formulas for every year using variables
# use // to remove decimals
year1 = total_population + (1 * births + deaths + immigrants) // 1
year2 = total_population + (2 * births + deaths + immigrants) // 1
year3 = total_population + (3 * births + deaths + immigrants) // 1
year4 = total_population + (4 * births + deaths + immigrants) // 1
year5 = total_population + (5 * births + deaths + immigrants) // 1


print("The US Census Bureaus' projected population for the next five years:")
print("Year 1 is", year1)
print("Year 2 is", year2)
print("Year 3 is", year3)
print("Year 4 is", year4)
print("Year 5 is", year5)

