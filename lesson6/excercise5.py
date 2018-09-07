#!/usr/bin/env python
#!/usr/bin/env python
"""
Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have
TextFSM automatically convert this show command output to structured data.
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
"device_type":"cisco_ios"
}

net_connect = Netmiko(**device1)

net_connect.enable()

command = "show ip int brie"

output = net_connect.send_command(command, use_textfsm=True)

net_connect.disconnect()


pprint(output)