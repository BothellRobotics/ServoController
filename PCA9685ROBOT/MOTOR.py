import sys

import time

class MOTOR:

    def __init__(self, forward_channel, reverse_channel, pwm_channel, \
                    reverse_sts, direction_last_scan, speed_command, \
                    count_last_scan, start_command, stop_command, \
                    reverse_command, running_sts, forward_sts, \
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

    #forward_channel - set
    @property
    def forward_channel(self, value):
        self._forward_channel = int(value)
    
    #forward_channel - get
    @property
    def forward_channel(self):
        return self._forward_channel

    #reverse_channel - set
    @property
    def reverse_channel(self, value):
        self._reverse_channel = int(value)
    
    #reverse_channel - get
    def reverse_channel(self):
        return self._reverse_channel

    #pwm_channel - set
    @property
    def pwm_channel(self, value):
        self._pwm_channel = int(value)
    
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
    def minimum_speed(self, value):
        self._minimum_speed = float(value)
    
    # maximum_speed set
    def maximum_speed(self, value):
        self._maximum_speed = float(value)
    
    def speed_command(self, value):
        self._speed_command = float(value)
    
    def count_last_scan(self, value):
        self._count_last_scan = int(value)

    def start_command(self, value):
        self._start_command = bool(value)
            
    def stop_command(self, value):
        self._stop_command = bool(value)    

    def reverse_command(self, value):
        self._reverse_command = bool(value)
        
    def running_sts(self, value):
        self._running_sts = bool(value)
        
    def forward_sts(self, value):
        self._forward_sts = bool(value)
    
    def direction_last_scan(self, value):
        self._direction_last_scan = bool(value)

    def reverse_sts(self, value):
        self._reverse_sts = bool(value)