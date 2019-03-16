from __future__ import division
import time
from PCA9685ROBOT import PCA9685ROBOT
import motor

class DEVICECONTROLLER:

    _servo_controller
    
    @property
    def servo_controller(self, value):
        self._servo_controller = value

    @property
    def forward_right_motor(self, value):
        self._forward_right_motor = value
    
    @property
    def forward_left_motor(self, value):        
        self._forward_left_motor = value

    @property
    def backward_right_motor(self, value):
        self._backward_right_motor = value

    @property
    def backward_left_motor(self, value):
        self._backward_left_motor = value
    

    def __init__(self, servo_controller, forward_right_motor, forward_left_motor, backward_right_motor, backward_left_motor):
        print('Initialize device controller')
        self._servo_controller = servo_controller
        self._forward_right_motor = forward_right_motor
        self._forward_left_motor = forward_left_motor
        self._backward_right_motor = backward_right_motor
        self._backward_left_motor = backward_left_motor

    def control_motor(self, dc_motor):
        counts = 0
        speed = dc_motor.speed_command
        if(speed > dc_motor.maximum_speed):
            speed = dc_motor.maximum_speed
        elif (speed < dc_motor.minimum_speed):
            speed = dc_motor.minimum_speed
        
        if(dc_motor.minimum_speed == dc_motor.maximum_speed):
            counts = _servo_controller.




