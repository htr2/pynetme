#!/usr/bin/env python
"""
connect to network devices one after the other. Use send_command() to execute a
show command on each of these devices. Prints output to the screen.
"""

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

import pdb
import logging
import nornir

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

#password = getpass()

import inventory

command = "dir"

for device in inventory.LON4LAB:
    net_connect = Netmiko(**device)
    net_connect.enable()
    output = net_connect.send_command(command, use_textfsm=True)
    net_connect.disconnect()
    print(device)
    pprint(output)