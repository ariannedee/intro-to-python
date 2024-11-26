x = 3

while x >= 0:  # Will keep looping until condition is False
    print(x)
    x = x - 1


y = 0
while True:  # Will keep looping until it encounters a break
    print(y)
    y += 1
    if y == 10:
        break


z = 10
while z > 0:
    z -= 1
    if z % 2 == 1:  # If z is odd (remainder of z / 2 is 1)
        continue    # Stop current loop (don't print) but go onto the next iteration
    print(z)
