temp = int(input("What temperature is your water? "))

if temp < 0:
    print("It's freezing")
elif temp > 100:
    print("It's boiling")
else:
    print("It's just water")
