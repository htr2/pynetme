#!/usr/bin/env python
"""
Find a command on your device that has additional prompting. Use send_command_timing to send the
command down the SSH channel. Capture the output and handle the additional prompting.
"""

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

import pdb


password = getpass()

device1 = {
"host":"10.25.254.97",
"username":"admin",
"password":password,
"device_type":"cisco_ios"
}

net_connect = Netmiko(**device1)

net_connect.enable()

filename = 'smallfile'
command = 'delete flash:{}'.format(filename)


output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)

if ']?' in output:
    # I don't confirm the file delete.
    output = net_connect.send_command_timing('n', strip_prompt=False, strip_command=False)
else:
    raise ValueError("Expected confirm message in output")


print("Output:",output)