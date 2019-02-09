print(f'True and True is {True and True}')
print(f'True and False is {True and False}')
print(f'False and False is {False and False}')
print()
print(f'True or True is {True or True}')
print(f'True or False is {True or False}')
print(f'False or False is {False or False}')
print()
print(f'not True is {not True}')
print(f'not False is {not False}')
print()

x = True
y = False
print(f'True and not True is {True and not True}')
print(f'(x or y) and not (x and y) is {(x or y) and not (x and y)} for x: {x} y: {y}')
y = True
print(f'(x or y) and not (x and y) is {(x or y) and not (x and y)} for x: {x} y: {y}')
