"""
Randomly returns two numbers between 1 and 6
"""
import random

# Generate two random integer between 1 and 6 (inclusive)
die_1 = random.randint(1, 6)
die_2 = random.randint(1, 6)

# Tell the user what the result was
print(f'You rolled a {die_1} and {die_2}')
