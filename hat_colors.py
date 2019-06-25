#! /usr/bin/env python

#script will define colors for a scrolling message on Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors
grey = (50, 50, 50)
maroon = (128, 0, 0)

speed = 0.05

message = "Howdy"

sense.show_message(message, speed, text_colour=maroon, back_colour=grey)

sense.clear()
