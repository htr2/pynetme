#!/usr/bin/env python
"""
In a Python shell, try importing the 'my_devices' when my_devices.py is not in your current
working directory.

What exception do you get when you do this?

Update your PYTHONPATH environment variable so that you are successfully able to import this
module.
"""
from __future__ import print_function, unicode_literals
from pprint import pprint
import sys

#modifying syspath
tmp_list = ["c:\\Users\\henning.voelksen\\Downloads\\python\\"]
sys.path = sys.path + tmp_list

import excercise1b_my_devices

pprint(excercise1b_my_devices.rtr1)