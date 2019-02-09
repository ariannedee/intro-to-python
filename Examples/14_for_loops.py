# Use range() to loop through a list of numbers
print('range(10)')
for i in range(10):
    print(i)
print()

print('range(10, 20)')
for i in range(10, 20):
    print(i)
print()

print('range(10, 20, 2)')
for i in range(10, 20, 2):
    print(i)
print()


primes = [1, 2, 3, 5, 7, 11, 13]
# Can loop over lists
for number in primes:
    print(number)
print()

# If you need to know the index, use enumerate()
for i, number in enumerate(primes):
    print(f'{i}: {number}')
