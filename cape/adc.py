
import ctypes
from .lib import lib

lib.initialize_mmap_adc()

_jack = lib.rc_dc_jack_voltage
_jack.restype = ctypes.c_float

_battery = lib.rc_battery_voltage
_battery.restype = ctypes.c_float

_get = lib.rc_adc_volt
_get.argstype = (ctypes.c_float)
_get.restype = ctypes.c_float

print('adc initialized')


def jack():
    v = _jack()
    if v < 2:
        return -1
    return v


def battery():
    min = _battery()
    max = min
    for i in range(9):
        v = _battery()
        if v < min:
            min = v
        elif v > max:
            max = v
    diff = max - min
    if diff > 0.2:
        return -1
    return v


# There is a 6-pin JST-SH socket on the Cape for connecting up to 4
# potentiometers or general use analog signals. The pinout of this socket is
# as follows:
#   1 - Ground
#   2 - VDD_ADC (1.8V)
#   3 - AIN0
#   4 - AIN1
#   5 - AIN2
#   6 - AIN3
def get(pin):
    if pin < 0 or pin > 6:
        return -1
    return _get(pin)

