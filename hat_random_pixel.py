#! /usr/bin/env python
# displays one letter at a time with random colors
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
#assign a random integer between 0 and 255 to a variable named r
r = random.randint (0,255)
print("The random Red number is"), r, ("this time")

g = random.randint (0,255)
print("The random Green number is"), g, ("this time")

b = random.randint (0,255)
print("The random Blue number is"), b, ("this time")

x = random.randint (0,7)
print("The random x coordinate is"), x, ("this time")

y = random.randint (0,7)
print("The random y coordinate is"), y, ("this time")

sense.set_pixel(x, y, (r,g,b))
time.sleep(5)

sense.clear()
