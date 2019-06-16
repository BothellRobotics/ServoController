from __future__ import division
import time
from PCA9685ROBOT import PCA9685ROBOT
from PCA9685ROBOT import MOTOR

class ROVER:
    
    #def __init__(self, fr = MOTOR(3, 2, 1), br = MOTOR(7, 8, 9), bl = MOTOR(12, 11, 10), fl = MOTOR(13, 14, 15)):
    def __init__(self, fr = MOTOR(12, 11, 10), br = MOTOR(12, 11, 10), fl = MOTOR(7, 8, 9), bl = MOTOR(13, 14, 15)):
        print('Initialize-8-7-9 device controller')
        self._servo_controller = PCA9685ROBOT()
        self._forward_right_motor = fr
        self._forward_left_motor = fl
        self._backward_right_motor = br
        self._backward_left_motor =  bl
        self._periodic_timer_milliseconds = 100
#back_right
#forward_right are same


    @property
    def servo_controller(self):
        return self._servo_controller
    
    @property
    def forward_right_motor(self):
        return self._forward_right_motor

    @property
    def forward_left_motor(self):        
        return self._forward_left_motor

    @property
    def backward_right_motor(self):
        return self._backward_right_motor
    
    @property
    def backward_left_motor(self):
        return self._backward_left_motor
    
    @forward_left_motor.setter
    def forward_left_motor(self, value):        
        self._forward_left_motor = value

    @servo_controller.setter
    def servo_controller(self, value):
        self._servo_controller = value

    @forward_right_motor.setter
    def forward_right_motor(self, value):
        self._forward_right_motor = value
    
    @backward_right_motor.setter
    def backward_right_motor(self, value):
        self._backward_right_motor = value

    @backward_left_motor.setter
    def backward_left_motor(self, value):
        self._backward_left_motor = value

    @property
    def update_rate(self):
        return _periodic_timer_milliseconds
    
    @update_rate.setter
    def update_rate(self, value):
        if(value < 1000):
            _periodic_timer_milliseconds = 1000
        elif(value > 1):
            _periodic_timer_milliseconds = 1
        else:
            _periodic_timer_milliseconds = value
                    
    
    def control_motor(self, dc_motor):
        counts = 0
        speed = dc_motor.speed_command

        # Apply speed limit
        if(speed > dc_motor.maximum_speed):
            speed = dc_motor.maximum_speed
        elif (speed < dc_motor.minimum_speed):
            speed = dc_motor.minimum_speed

        # Scale the speed reference to PCA9685 device 'count'
        if(dc_motor.minimum_speed == dc_motor.maximum_speed):
            counts = self.servo_controller.minimum_count
        else:
            counts = int((speed - dc_motor.minimum_speed) * 
            float((self.servo_controller.maximum_count - self.servo_controller.minimum_count) / (dc_motor.maximum_speed - dc_motor.minimum_speed))  + 
            float(self.servo_controller.minimum_count))

        # Sart
        if(dc_motor.start_command and not dc_motor.running_sts):
            if(dc_motor.reverse_command):
                print('reversing the rover')
                self.servo_controller.set_channel_off(dc_motor.forward_channel)
                dc_motor.forward_sts = False
                self.servo_controller.set_channel_on(dc_motor.reverse_channel)
                dc_motor.reverse_sts = True
            else:
                print('rover moves forward')
                self.servo_controller.set_channel_off(dc_motor.reverse_channel)
                dc_motor.reverse_sts = False                
                self.servo_controller.set_channel_on(dc_motor.forward_channel)
                dc_motor.forward_sts = True
        
            dc_motor.direction_last_scan = dc_motor.reverse_command
            self.servo_controller.set_pwm(dc_motor.pwm_channel, self.servo_controller.minimum_count, counts)
            dc_motor.count_last_scan = counts
            dc_motor.running_sts = True
        # Stop
        if(dc_motor.stop_command and dc_motor.running_sts):
            self.servo_controller.set_channel_off(dc_motor.reverse_channel)
            self.servo_controller.set_channel_off(dc_motor.forward_channel)
            self.servo_controller.set_channel_off(dc_motor.pwm_channel)
            dc_motor.count_last_scan = counts
            dc_motor.running_sts = False
            dc_motor.stop_command = False

        # Speed
        if(counts != dc_motor.count_last_scan and dc_motor.running_sts):
            self.servo_controller.set_pwm(dc_motor.pwm_channel, self.servo_controller.minimum_count, counts)
            dc_motor.count_last_scan = counts

        # Direction
        if(dc_motor.running_sts and (dc_motor.reverse_command != dc_motor.direction_last_scan)):
            if(dc_motor.reverse_command):
                self.servo_controller.set_channel_off(dc_motor.forward_channel)
                dc_motor.forward_sts = False
                self.servo_controller.set_channel_on(dc_motor.reverse_channel)
                dc_motor.reverse_sts = True
            else:
                self.servo_controller.set_channel_off(dc_motor.reverse_channel)
                dc_motor.reverse_sts = False
                self.servo_controller.set_channel_on(dc_motor.forward_channel)
                dc_motor.forward_sts = True

            dc_motor.direction_last_scan = dc_motor.reverse_command

        dc_motor.start_command = False
        dc_motor.stop_command = False

    def control_rover(self):
        self.control_motor(self._backward_left_motor)
        self.control_motor(self._backward_right_motor)
        self.control_motor(self._forward_right_motor)
        self.control_motor(self._forward_left_motor)
                
    def start_rover(self):
        self._backward_left_motor.start_command = True
        self._backward_right_motor.start_command = True
        self._forward_right_motor.start_command = True
        self._forward_left_motor.start_command = True
        self.control_rover()

    def stop_rover(self):
        self._backward_right_motor.stop_command = True
        self._forward_right_motor.stop_command = True
        self._forward_left_motor.stop_command = True
        self._backward_left_motor.stop_command = True
        self.control_rover()    

    def forward_rover(self):
        self._backward_left_motor.reverse_command = True
        self._backward_right_motor.reverse_command = True
        self._forward_right_motor.reverse_command = True
        self._forward_left_motor.reverse_command = True
        self.control_rover()

    def forward_back_left_motor(self):
        self._backward_left_motor.reverse_command = True
        #self._backward_right_motor.reverse_command = True
        #self._forward_right_motor.reverse_command = True
        #self._forward_left_motor.reverse_command = True
        self.control_rover()


    def forward_backward_left_motor(self):
        self._backward_left_motor.reverse_command = True        
        self.control_motor(self._backward_left_motor)
    
    def reverse_rover(self):
        self._backward_left_motor.reverse_command = False
        self._backward_right_motor.reverse_command = False
        self._forward_right_motor.reverse_command = False
        self._forward_left_motor.reverse_command = False
        self.control_rover()

    def left_rover(self):
        self._backward_right_motor.reverse_command = True
        self._forward_right_motor.reverse_command = True
        self._backward_left_motor.reverse_command = False
        self._forward_left_motor.reverse_command = False
        #self._backward_left_motor.stop_command = True
        #self._forward_left_motor.stop_command = True

        self.control_rover()

    def right_rover(self):
        self._forward_left_motor.reverse_command = True
        self._backward_left_motor.reverse_command = True
        self._backward_right_motor.reverse_command = False
        self._forward_right_motor.reverse_command = False
        #self._backward_right_motor.stop_command = True
        #self._backward_left_motor.stop_command = True

        self.control_rover()

    def set_controller_frequency(self, frequency):
        self.servo_controller.frequency = frequency

    def set_rover_speed(self, speed_value):
        self._backward_left_motor.speed_command = speed_value
        self._forward_left_motor.speed_command = speed_value
        self._backward_right_motor.speed_command = speed_value
        self._forward_right_motor.speed_command = speed_value
        
        self.control_rover()

        





