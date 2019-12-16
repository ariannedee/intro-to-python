"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""
# Ask for a temperature in Fahrenheit
temp_in_f = float(input('Temp in F: '))

# Calculate it in Celsius
temp_in_c = (temp_in_f - 32) * 5/9

# Tell the user what it is
print('Temp in C: {}'.format(temp_in_c))
