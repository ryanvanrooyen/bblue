#! /usr/bin/env python3

import cape.adc as adc
import time

is_plugged_in = False

while True:
    out = 'Jack/Battery V: {:.2f} / {:.2f}'
    print(out.format(adc.jack(), adc.battery()), end='\r')
    time.sleep(1)

