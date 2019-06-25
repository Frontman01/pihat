#! /usr/bin/env python
# displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.show_letter("H", (34,139,34))
time.sleep(1)
sense.show_letter("i", (75,0,130))
time.sleep(1)
sense.show_letter("!", (255,219,88))
time.sleep(1)

sense.clear()
