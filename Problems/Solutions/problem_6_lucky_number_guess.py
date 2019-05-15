"""
This code should get the user to guess a random number between 1 and 10.
If the user is right, congratulate them.
If they're wrong, say if the answer is higher or lower.
Then say what the answer was.
"""

import random
answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

if guess == answer:
    print('Correct!')
elif guess < answer:
    print('Higher')
else:
    print('Lower')

print('The number was {}'.format(answer))
