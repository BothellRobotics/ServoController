from __future__ import division
import time
import pca9685_robot
import motor

class device_controller:

    _servo_controller = pca9685_robot()
    _forward_right_motor = motor()
    _forward_left_motor = motor()
    _backward_right_motor = motor()    
    _backward_left_motor = motor()
    

    def __init__(self):
        self._servo_controller = pca9685_robot()
        self._forward_right_motor = motor()
        self._forward_left_motor = motor()
        self._backward_right_motor = motor()    
        self._backward_left_motor = motor()

    def control_motor(self, dc_motor):
        counts = 0
        speed = dc_motor.speed_command
        if(speed > dc_motor.maximum_speed):
            speed = dc_motor.maximum_speed
        elif (speed < dc_motor.minimum_speed):
            speed = dc_motor.minimum_speed
        
        if(dc_motor.minimum_speed == dc_motor.maximum_speed):
            counts = _servo_controller.




