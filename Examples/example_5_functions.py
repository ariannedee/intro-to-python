def add(a, b):
    return a + b


def say_hello(name, shout=False):
    greeting = 'Hello ' + name
    if shout:
        greeting = greeting.upper()
    return greeting


print(say_hello('beyoncé'))
print(say_hello('beyoncé', True))
print(say_hello(name='beyoncé', shout=True))
