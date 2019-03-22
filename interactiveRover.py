# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
from PCA9685ROBOT import PCA9685ROBOT
from PCA9685ROBOT import ROVER
from PCA9685ROBOT import MOTOR

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = PCA9685ROBOT()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_med = 600  # Max pulse length out of 4096
servo_max = 2000

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

fwd_rht = MOTOR(6, 5, 4)
bwd_rht = MOTOR(7, 8, 9)
bwd_lft = MOTOR(12, 11, 10)
fwd_lft = MOTOR(13, 14, 15)

rover = ROVER()

print('Moving servo on channel 0, press Ctrl-C to quit...')
print('Press F: Forward')
print('Press B: Backward')
print('Press L: Turn LEFT')
print('Press R: Turn RIGHT')
print('Press I: Increase Speed')
print('Press D: Decrease Speed')
print('Press S: Stop')
print('Press one of the above options')
try:
    while True:        
        cmd = input()
        if(cmd == 'F' or cmd == 'f'):
            #rover.stop_rover()
            rover.start_rover()
            time.sleep(1)
            rover.forward_rover()
            rover.set_rover_speed(40)
            time.sleep(5)
        elif(cmd == 'B' or cmd == 'b'):
            #rover.stop_rover()                        
            rover.reverse_rover()
            time.sleep(1)
            rover.set_rover_speed(40)
            time.sleep(10)
        elif(cmd == 'L' or cmd == 'l'):
            #rover.stop_rover()            
            rover.left_rover()            
            time.sleep(5)
        elif(cmd == 'R' or cmd == 'r'):
            #rover.stop_rover()            
            rover.right_rover()
            time.sleep(5)
        elif(cmd == 'I' or cmd == 'i'):
            rover.set_rover_speed(99.5)
            time.sleep(5)
        elif(cmd == 'D' or cmd == 'd'):
            rover.set_rover_speed(30.5)
            time.sleep(5)
        elif(cmd == 'S' or cmd == 's'):
            rover.stop_rover()
except KeyboardInterrupt:
    print('Attempt Program interrupt')
    rover.stop_rover()
    print('Program interrupted')
