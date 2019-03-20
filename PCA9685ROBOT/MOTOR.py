import sys

import time

class MOTOR:

    def __init__(self, forward_channel, reverse_channel, pwm_channel, \
                    reverse_sts = False, direction_last_scan = False, \
                    speed_command = float(20.5), \
                    count_last_scan = int(0), start_command = True, \
                    stop_command = False, \
                    reverse_command = True, running_sts = False, \
                    forward_sts = True, \
                    minimum_speed = 0, maximum_speed = 100):
        self._forward_channel = forward_channel
        self._reverse_channel = reverse_channel
        self._pwm_channel = pwm_channel
        self._minimum_speed = minimum_speed
        self._maximum_speed = maximum_speed
        self._speed_command = speed_command
        self._count_last_scan = count_last_scan
        self._start_command = start_command
        self._stop_command = stop_command
        self._reverse_command = reverse_command
        self._running_sts = running_sts
        self._forward_sts = forward_sts
        self._reverse_sts = reverse_sts
        self._direction_last_scan = direction_last_scan
        print('Initialized Motor object')

    #forward_channel - get
    @property
    def forward_channel(self):
        return self._forward_channel
    
    #reverse_channel - get
    def reverse_channel(self):
        return self._reverse_channel
    
    #pwm_channel - get
    @property
    def pwm_channel(self):
        return self._pwm_channel
    
    # minimum_speed get
    @property
    def minimum_speed(self):
        return self._minimum_speed
    
    # maximum_speed get
    @property
    def maximum_speed(self):
        return self._maximum_speed    
    
    @property
    def speed_command(self):
        return self._speed_command

    @property
    def count_last_scan(self):
        return self._count_last_scan
    
    @property
    def start_command(self):
        return self._start_command    

    @property
    def running_sts(self):
        return self._running_sts

    @property
    def stop_command(self):
        return self._stop_command
        
    @property
    def reverse_command(self):
        return self._reverse_command
        
    @property
    def forward_sts(self):
        return self._forward_sts

    @property
    def reverse_sts(self):
        return self._reverse_sts    
    
    @property
    def direction_last_scan(self):
        return self._direction_last_scan

    # minimum_speed set    
    @minimum_speed.setter
    def minimum_speed(self, value):
        self._minimum_speed = float(value)
    
    # maximum_speed set
    @maximum_speed.setter
    def maximum_speed(self, value):
        self._maximum_speed = float(value)
    
    @speed_command.setter
    def speed_command(self, value):
        self._speed_command = float(value)
    
    @count_last_scan.setter
    def count_last_scan(self, value):
        self._count_last_scan = int(value)

    @start_command.setter
    def start_command(self, value):
        self._start_command = bool(value)

    @stop_command.setter    
    def stop_command(self, value):
        self._stop_command = bool(value)    

    @reverse_command.setter
    def reverse_command(self, value):
        self._reverse_command = bool(value)
        
    @running_sts.setter
    def running_sts(self, value):
        self._running_sts = bool(value)
        
    @forward_sts.setter
    def forward_sts(self, value):
        self._forward_sts = bool(value)
    
    @direction_last_scan.setter
    def direction_last_scan(self, value):
        self._direction_last_scan = bool(value)

    @reverse_sts.setter
    def reverse_sts(self, value):
        self._reverse_sts = bool(value)

    #forward_channel - set
    @forward_channel.setter
    def forward_channel(self, value):
        self._forward_channel = int(value)
    
    #reverse_channel - set
    @reverse_channel.setter
    def reverse_channel(self, value):
        self._reverse_channel = int(value)

    #pwm_channel - set
    @pwm_channel.setter
    def pwm_channel(self, value):
        self._pwm_channel = int(value)
