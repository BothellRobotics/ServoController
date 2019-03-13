import sys

if sys.version_info < (3.4):
    raise SystemError('Must be using Python 3.4 or higher')

import time

class motor:

    def __init__(self, forward_channel, reverse_channel, pwm_channel, minimum_speed = 0, maximum_speed = 100):
        self._forward_channel = forward_channel
        self._reverse_channel = reverse_channel
        self._pwm_channel = pwm_channel
        self._minimum_speed = minimum_speed
        self._maximum_speed = maximum_speed        
        print('Initialized Motor object')

    _forward_channel

    @property
    def forward_channel(self, value):
        self._forward_channel = int(value)
    
    @property
    def forward_channel(self):
        return self._forward_channel

    _reverse_channel

    @property
    def reverse_channel(self, value):
        self._reverse_channel = int(value)
    
    @property_servo_controller = Adafruit_PCA9685.PCA9685()
    _forward_right_motor = motor()
    _forward_left_motor = motor()
    _backward_right_motor = motor()    
    _backward_left_motor = motor()
    def reverse_channel(self):
        return self._reverse_channel


    _pwm_channel

    @property
    def pwm_channel(self, value):
        self._pwm_channel = int(value)
    
    @property
    def pwm_channel(self):
        return self._pwm_channel

    _minimum_speed

    @property
    def minimum_speed(self, value):
        self._minimum_speed = float(value)
    
    @property
    def minimum_speed(self):
        return self._minimum_speed

    _maximum_speed

    @property
    def maximum_speed(self, value):
        self._maximum_speed = float(value)
    
    @property
    def maximum_speed(self):
        return self._maximum_speed

    _speed_command

    @property
    def speed_command(self, value):
        self._speed_command = float(value)
    
    @property
    def speed_command(self):
        return self._speed_command
    
    _count_last_scan

    @property
    def count_last_scan(self, value):
        self._count_last_scan = int(value)
    
    @property
    def count_last_scan(self):
        return self._count_last_scan

    _start_command

    @property
    def start_command(self, value):
        self._start_command = bool(value)
    
    @property
    def start_command(self):
        return self._start_command

    _stop_command

    @property
    def stop_command(self, value):
        self._stop_command = bool(value)
    
    @property
    def stop_command(self):
        return self._stop_command

    _reverse_command

    @property
    def reverse_command(self, value):
        self._reverse_command = bool(value)
    
    @property
    def reverse_command(self):
        return self._reverse_command
    

    _running_sts

    @property
    def running_sts(self, value):
        self._running_sts = bool(value)
    
    @property
    def running_sts(self):
        return self._running_sts

    _forward_sts

    @property
    def forward_sts(self, value):
        self._forward_sts = bool(value)
    
    @property
    def forward_sts(self):
        return self._forward_sts

    _reverse_sts

    @property
    def reverse_sts(self, value):
        self._reverse_sts = bool(value)
    
    @property
    def reverse_sts(self):
        return self._reverse_sts
    
    _direction_last_scan

    @property
    def direction_last_scan(self, value):
        self._direction_last_scan = bool(value)
    
    @property
    def direction_last_scan(self):
        return self._direction_last_scan
