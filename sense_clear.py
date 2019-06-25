#! /usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat ()

# script will clear any LEDs left in 'on' state

print("clearing LEDs")

sense.clear()
