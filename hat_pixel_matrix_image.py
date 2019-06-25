#! /usr/bin/env python
# displays one letter at a time with random colors
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
r = (255,0,0)
b = (0,0,255)
w = (255,255,255)

pixels = [
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w,
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w,
]

sense.set_pixels(pixels)
time.sleep(1)
pixels = [
    b,b,b,b,w,w,w,w,
    b,b,b,b,w,w,w,w,
    b,b,b,b,w,w,w,w,
    b,b,b,b,w,w,w,w,
    b,b,b,b,r,r,r,r,
    b,b,b,b,r,r,r,r,
    b,b,b,b,r,r,r,r,
    b,b,b,b,r,r,r,r,
]

sense.set_pixels(pixels)
time.sleep(1)
sense.clear()

