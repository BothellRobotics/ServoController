try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'PCA9685ROBOT',
      version           = '1.0.0',
      author            = 'Babu Govindarajan',
      author_email      = 'info@bothellrobotics.com',
      description       = 'Python code to use the PCA9685 PWM servo/LED controller with a Raspberry Pi.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/BothellRobotics/ServoController/',
      dependency_links  = ['https://github.com/BothellRobotics/ServoController/tarball/master#egg=Adafruit-GPIO-0.6.5'],
      install_requires  = ['Adafruit-GPIO>=0.6.5'],
      packages          = find_packages())