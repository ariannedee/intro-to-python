time = 10

if time < 7:
    sleeping = True
elif time > 22:
    sleeping = True
else:
    sleeping = False

print(sleeping)
print('sleeping') if sleeping else print('awake')
