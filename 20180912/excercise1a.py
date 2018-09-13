#!/usr/bin/env python
"""
test
"""

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from nornir.core import InitNornir
from nornir.plugins.tasks import commands
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

import pdb
import logging

nr = InitNornir()


result = nr.run(
    task=netmiko_send_command,
    command_string="show run"
)

print_result(result)





"""
pdb.set_trace()

result = nr.run(task=commands.remote_command, 
                command="show run")

print_result(result)
"""