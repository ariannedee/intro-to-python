def add(a, b):
    a = float(a)
    b = float(b)
    return a + b


print(add(1, 2))
print(add('1', '2'))


def say_hello(name, shout=False):  # Can have optional parameters (e.g. shout)
    greeting = 'Hello ' + name
    if shout:
        greeting = greeting.upper()
    return greeting


print(say_hello('beyoncé'))                   # 1 required argument
print(say_hello('beyoncé', True))             # Positional arguments
print(say_hello('beyoncé', shout=False))      # Positional has to come before keyword arguments
print(say_hello(shout=True, name='beyoncé'))  # Keyword args can be in any order
