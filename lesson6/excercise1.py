#!/usr/bin/env python
"""Establish a connection to the network device and print out the device's prompt."""

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

password = getpass()

device1 = {
"host":"10.25.254.97",
"username":"admin",
"password":password,
"device_type":"cisco_ios"
}

net_connect = Netmiko(**device1)

print(net_connect.find_prompt())
#new 