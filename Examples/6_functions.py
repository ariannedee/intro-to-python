def add(a, b):
    return a + b


def say_hello(name):
    return f'Hello {name}'


def is_palindrome(string):
    def reverse(word):
        return word[::-1]

    midpoint = len(string)//2
    first_half = string[:midpoint]
    second_half = string[midpoint * -1:]
    return first_half == reverse(second_half)


def add_list(n, *args):
    print(*args)


print(add_list(2, 6, 9, 10))


def say_hello(name, capitalize=False):
    if capitalize:
        name = name.capitalize()
    return 'Hello ' + name


print(say_hello('arianne', False))
