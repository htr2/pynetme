#!/usr/bin/env python
"""
Use send_command() to send a show command down the SSH channel. Retrieve the results and print the
results to the screen.
"""
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

try:
    command = raw_input("Enter command to run: ")
except NameError:
    command = input("Enter command to run: ")

net_connect = Netmiko(**device1)

output = net_connect.send_command(command)


print(output)