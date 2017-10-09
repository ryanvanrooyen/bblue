
import ctypes
import os

_file = 'roboticscape.so'
_current_dir = os.path.split(__file__)[:1][0]
_path = os.path.join(_current_dir, _file)

lib = ctypes.cdll.LoadLibrary(_path)

print('roboticscape.so library loaded.')

