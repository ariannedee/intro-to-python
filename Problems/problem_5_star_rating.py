"""
Bonus problem
Fill out the star_rating function that takes an integer from 0 to 5.
It returns a string with 5 stars, with that number of them are filled in.

The 'assert' function will make the program fail if False is passed in.
It can be used for easy testing, but libraries like unittest and pytest can be more useful.
"""


def star_rating(rating):
    stars = '★★★★★☆☆☆☆☆'
    return stars  # <-- Replace with your code


# Test star_rating function
assert(star_rating(0) == '☆☆☆☆☆')
assert(star_rating(1) == '★☆☆☆☆')
assert(star_rating(4) == '★★★★☆')
assert(star_rating(5) == '★★★★★')

print('All tests passed')
