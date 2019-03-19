from __future__ import division
import logging
import time
import math

#Registers
PCA9685_ADDRESS  = 0x40
MODE1            = 0x00
MODE2            = 0x01
SUBADR1          = 0x02
SUBADR2          = 0x03
SUBADR3          = 0x04
PRESCALE         = 0xFE
LED0_ON_L        = 0x06
LED0_ON_H        = 0x07
LED0_OFF_L       = 0x08
LED0_OFF_H       = 0x09
ALL_LED_ON_L     = 0xFA
ALL_LED_ON_H     = 0xFB
ALL_LED_OFF_L    = 0xFC
ALL_LED_OFF_H    = 0xFD

# Bits
RESTART          = 0x80
SLEEP            = 0x10
ALLCALL          = 0x01
INVRT            = 0x10
OUTDRV           = 0x04

logger = logging.getLogger(__name__)

def software_reset(i2c=None, **kwargs):
    """Sends a software reset (SWRST) command to all servo drivers on the bus."""
    # Setup I2C interface for device 0x00 to talk to all of them
    if i2c is None:
        import Adafruit_GPIO.I2C as I2C
        i2c = I2C
    self._device = i2c.get_i2c_device(0x00, **kwargs)
    self._device.writeRaw8(0x06)

class PCA9685ROBOT(object):
    """PCA9685 PWM LED/servo controller."""

    def __init__(self, address=PCA9685_ADDRESS, i2c=None, minimum_count = 0, maximum_count = 4095, minimum_frequency = 0, maximum_frequency = 1000, **kwargs):
        """Initialize the PCA9685"""
        # Setup I2C interface for the device
        print('Initialize the PCA9685')
        self._minimum_count  = minimum_count
        self._maximum_count  = maximum_count
        self._minimum_frequency = minimum_frequency
        self._maximum_frequency = maximum_frequency
        self._frequency
        self._ready
        self._address
        # Setup I2C interface for the device
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
            print('Initialized i2c GPIO')
        self._device = i2c.get_i2c_device(address, **kwargs)
        self.set_all_pwm(0,0)
        self._device.write8(MODE2, OUTDRV)
        self._device.write8(MODE1, ALLCALL)
        time.sleep(0.005)   # wait for oscillator
        mode1 = self._device.readU8(MODE1)
        mode1 = mode1 & ~SLEEP  # wake up (reset sleep)
        self._device.write8(MODE1, mode1)
        time.sleep(0.005)   # wait for oscillator

    @property
    def ready(self):
        return self._ready

    @property
    def address(self):
        return self._address

    @property
    def minimum_frequency(self):
        return self._minimum_frequency

    @property
    def maximum_frequency(self):
        return self._maximum_frequency
    
    @property
    def minimum_count(self):
        return self._minimum_count

    @property
    def maximum_count(self):
        return self._maximum_count

    @property
    def frequency(self):
        return self._frequency

    @property
    def minimum_count(self, value):
        self._minimum_count = int(value)

    @property
    def maximum_count(self, value):
        self._maximum_count = int(value)
    
    @property
    def frequency(self, value):
        if(value < minimum_frequency):
            self._frequency = _minimum_frequency
        elif (value > maximum_frequency):
            self._frequency = _maximum_frequency
        else:
            self._frequency = value
        
        self.set_pwm_freq(self._frequency)

    def set_pwm_freq(self, freq_hz):
        """Set the PWM frequency to the provided value in hertz"""
        prescaleval = 25000000.00
        prescaleval /= 4096.0
        prescaleval /= float(freq_hz)
        prescaleval -= 1.0
        logger.debug('Setting PWM frequency to {0} Hz'.format(freq_hz))
        logger.debug('Estimated pre-scale: {0}'.format(prescaleval))
        prescale = int(math.floor(prescaleval + 0.5))
        logger.debug('Final pre-scale: {0}'.format(prescale))
        oldmode = self._device.readU8(MODE1);
        newmode = (oldmode & 0x7F) | 0x10
        self._device.write8(MODE1, newmode)
        self._device.write8(PRESCALE, prescale)
        self._device.write8(MODE1, oldmode)
        time.sleep(0.005)
        self._device.write8(MODE1, oldmode | 0x80)

    def set_pwm(self, channel, on_count, off_count):
        """Sets a single PWM channel."""
        print('attempting to set single pwm channel')
        self._device.write8(LED0_ON_L+4*channel, on_count & 0xFF)
        self._device.write8(LED0_ON_H+4*channel, on_count >> 8)
        self._device.write8(LED0_OFF_L+4*channel, on_count & 0xFF)
        self._device.write8(LED0_OFF_H+4*channel, off_count >> 8)

    def set_channel_off(self, channel):
        """Disable PWM on channel. Channel output set to OFF"""
        print('Attempting to set Channel output off')
        self._device.write8(LED0_ON_L+4*channel, 0x0000 & 0xFF)
        self._device.write8(LED0_ON_H+4*channel, 0x0000 >> 8)
        self._device.write8(LED0_OFF_L+4*channel, 0x1000 & 0xFF)
        self._device.write8(LED0_OFF_H+4*channel, 0x1000 >> 8)

    def set_channel_on(self, channel):
        """Disable PWM on channel. Channel output set to OFF"""
        print('Attempting to set Channel output off')
        self._device.write8(LED0_ON_L+4*channel, 0x1000 & 0xFF)
        self._device.write8(LED0_ON_H+4*channel, 0x1000 >> 8)
        self._device.write8(LED0_OFF_L+4*channel, 0x0000 & 0xFF)
        self._device.write8(LED0_OFF_H+4*channel, 0x0000 >> 8)

    def set_all_pwm(self, on_count, off_count):
        """Sets all PWM channels."""
        self._device.write8(LED0_ON_L, on_count & 0xFF)
        self._device.write8(LED0_ON_H, on_count >> 8)

        self._device.write8(LED0_OFF_L, on_count & 0xFF)
        self._device.write8(LED0_OFF_H, off_count >> 8)

    def set_all_pwm_off(self):
        print('Attempting to set all channel off')
        self._device.write8(ALL_LED_OFF_L, 0x00)
        self._device.write8(ALL_LED_OFF_H, 0x10)            

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        pwm.set_pwm(channel, 0, pulse)




