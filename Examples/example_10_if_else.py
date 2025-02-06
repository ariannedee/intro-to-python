salutation = 'Hello world'
shouting = False

if shouting:
    print(salutation.upper())
else:
    print(salutation)


hungry = True

if hungry:  # else is not needed
    print('Find something to eat')
print('Continue your day')


temp = int(input("What temperature is your water? "))

if temp <= 0:
    print("It's freezing")
elif temp >= 100:  # Can have multiple elif (else if)
    print("It's boiling")
elif temp >= 50:
    print("It's hot")
else:
    print("It's just water")

print("Another")

# Conditions don't have to be True or False
name = input("Name: ")

if name:  # Will evaluate bool(name)
    print("Hello " + name)
else:
    print("Hello world")


# Comparing to True, False and None should use "is" keyword
name_was_input = bool(name)

if name_was_input is False:
    print("Invalid name")
