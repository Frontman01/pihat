#! /usr/bin/env python
# script will show a scrolling message on Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

# send the text "Hello World! to the show_message() function
sense.show_message("Howdy!")
