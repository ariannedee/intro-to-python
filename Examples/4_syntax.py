import random

number = random.randint(1, 11)
guess = int(input('Guess a number between 1 and 10: '))

if guess == number:
    print(f"You're right! it was {number}")
elif number >= guess - 2 and number <= guess + 2:
    print(f"Close! It's {number}")
else:
    print(f"Nope, it's {number}")