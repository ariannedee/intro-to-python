def star_rating(n):
    """Provides a string of stars with rating n (out of 5)"""
    stars = '★★★★★☆☆☆☆☆'
    return stars  # Fill out function here


assert(star_rating(0) == '☆☆☆☆☆')
assert(star_rating(1) == '★☆☆☆☆')
assert(star_rating(4) == '★★★★☆')
assert(star_rating(5) == '★★★★★')
