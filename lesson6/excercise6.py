#!/usr/bin/env python
"""
Optional, connect to three networking devices one after the other. Use send_command() to execute a
show command on each of these devices. Print this output to the screen.
"""

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

import pdb
import logging
logging.basicConfig(filename=r"C:\Users\henning.voelksen\Downloads\python\pynetme\lesson6\test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

password = getpass()

device1 = {
"host":"10.25.254.97",
"username":"admin",
"password":password,
"device_type":"cisco_ios",
"command":"show ip int brie" 
}

device2 = {
"host":"10.25.254.97",
"username":"admin",
"password":password,
"device_type":"cisco_ios",
"command":"show vrf"
}

devices = [device1,device2]


for device in devices:
    command = device.pop('command')
    net_connect = Netmiko(**device1)
    net_connect.enable()
    output = net_connect.send_command(command, use_textfsm=True)
    net_connect.disconnect()
    print(device)
    pprint(output)