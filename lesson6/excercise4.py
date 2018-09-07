#!/usr/bin/env python
"""
Use send_config_set() and send_config_from_file() to make configuration changes.
The configuration changes should be benign. For example, on Cisco IOS I typically change the
logging buffer size.
As part of your program verify that the configuration change occurred properly. For example, use
send_command() to execute 'show run' and verify the new configuration.
"""

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

import pdb
import logging
logging.basicConfig(filename=r"C:\Users\henning.voelksen\Downloads\python\pynetme\lesson6\test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

password = getpass()

device1 = {
"host":"10.25.254.97",
"username":"admin",
"password":password,
"device_type":"cisco_ios"
}

net_connect = Netmiko(**device1)

net_connect.enable()

print("Before:",net_connect.send_command("show run | inc logging"))

cfg_commands = ["logging buffered 8000", "no logging console"]

output = net_connect.send_config_set(cfg_commands)

print("After:",net_connect.send_command("show run | inc logging"))

net_connect.disconnect()


print("Output:",output)