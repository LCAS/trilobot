#!/usr/bin/env python3
# tri1.py
# esklar/16-feb-2024
#
# this is a little test programme for driving a trilobot.
#--


# import standard packages
import time
# import trilobot package 
from trilobot import Trilobot

# set parameters for controlling how far the trilobot moves
DRIVE_SPEED = 1.0
TURN_SPEED  = 1.0


# initialise a "tbot" object
print( 'hello!' )
tbot = Trilobot()

while True:
    distance = tbot.read_distance()
    if distance < 40:
        tbot.turn_left( TURN_SPEED )
        tbot.fill_underlighting(( 255, 0, 0 ))
    else:
        tbot.forward(DRIVE_SPEED)
        tbot.fill_underlighting(( 0, 255, 0 ))



# all done
print( 'goodbye!' )
