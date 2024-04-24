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
DRIVE_TIME  = 1.2
TURN_SPEED  = 1.4
TURN_TIME   = 1.6

# define motion functions
def go_forward():
    print( 'moving forward' )
    tbot.forward( DRIVE_SPEED )
    time.sleep( DRIVE_TIME )
    tbot.stop()
    
def go_backward():
    print( 'moving backward' )
    tbot.backward( DRIVE_SPEED )
    time.sleep( DRIVE_TIME )
    tbot.stop()

def turn_left():
    print( 'turning left' )
    tbot.curve_forward_left( TURN_SPEED )
    time.sleep( TURN_TIME )
    tbot.stop()

def turn_right():
    print( 'turning right' )
    tbot.curve_forward_right( TURN_SPEED )
    time.sleep( TURN_TIME )
    tbot.stop()

# define functions that turn on underlights
def red_lights():
    print( 'red lights' )
    tbot.fill_underlighting(( 255, 0, 0 ))

def green_lights():
    print( 'green lights' )
    tbot.fill_underlighting(( 0, 255, 0 ))

def blue_lights():
    print( 'blue lights' )
    tbot.fill_underlighting(( 0, 0, 255 ))

def yellow_lights():
    print( 'yellow lights' )
    tbot.fill_underlighting(( 255, 255, 0 ))

# define distance sensor function
def get_distance():
    distance = tbot.read_distance()
    print( 'distance from nearest object = %fcm' % ( distance ))
    return( distance )



#-----
# main
#-----

# initialise a "tbot" object
print( 'hello!' )
tbot = Trilobot()

# drive
go_forward()

# all done
print( 'goodbye!' )
