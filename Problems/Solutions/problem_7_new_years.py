"""
Start at 10 seconds and count down until 1 and then print "Happy New Year! 🎉"
"""
import time

seconds_left = 10

while seconds_left > 0:
    print(seconds_left)
    seconds_left -= 1
    time.sleep(1)

print('Happy New Year! 🎉')
