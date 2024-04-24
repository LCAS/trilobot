#!/usr/bin/env python3
# tri_drive.py
# esklar/16-feb-2024
#
# this is a little test programme for driving a trilobot using a simple command line controller.
#
#--


# import standard packages
import time
# import trilobot package 
from trilobot import Trilobot

# set parameters for controlling how far the trilobot moves
DRIVE_SPEED = 1.0
DRIVE_TIME  = 1.2
TURN_SPEED  = 1.0
TURN_TIME   = 0.8


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



#-----
# main
#-----

# initialise a "tbot" object
tbot = Trilobot()

# loop until user quits
more = True
while ( more ):
    # display menu of options to user
    print( '+-------------+--------------+----------+-----------+----------+' )
    print( '| i = forward | m = backward | j = left | k = right | q = quit |' )
    print( '+-------------+--------------+----------+-----------+----------+' )
    # read user's input
    c = input( 'please enter command> ' )
    # branch on user's input
    if ( c == 'q' or c == 'Q' ):
        more = False
    elif ( c == 'i' or c == 'I' ):
        go_forward()
    elif ( c == 'm' or c == 'M' ):
        go_backward()
    elif ( c == 'j' or c == 'J' ):
        turn_left()
    elif ( c == 'k' or c == 'K' ):
        turn_right()
    else:
        print( 'illegal command. please try again.' )
# end of loop
print( 'bye!' )
