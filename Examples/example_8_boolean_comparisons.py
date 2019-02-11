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

print(f'True and not True is {True and not True}')  # Always False
print(f'True or not True is {True or not True}')    # Always True

rain = True
snow = False
print((rain and snow) or (not rain and not snow))  # Use brackets to group
