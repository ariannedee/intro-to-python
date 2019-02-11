def add(a, b):
    return a + b


def say_hello(name, capitalize=False):
    if capitalize:
        name = name.capitalize()
    return 'Hello ' + name


print(say_hello('arianne'))
print(say_hello('arianne', True))
