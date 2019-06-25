#! /usr/bin/env python
# displays one letter at a time with random colors
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
#assign a random integer between 0 and 255 to a variable named r
r = random.randint (0,255)
print("The random number is"), r, ("this time")

n = random.randint (0,255)
print("The other random number is"), n, ("this time")

sense.show_letter("H", (r,n,0))
time.sleep(1)
sense.show_letter("i", (0,r,n))
time.sleep(1)
sense.show_letter("!", (n,0,r))
time.sleep(1)

sense.clear()
