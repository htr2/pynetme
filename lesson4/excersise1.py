#!/usr/bin/env python
""""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""
from __future__ import unicode_literals, print_function
import os
from pprint import pprint

net_device1 = {
    "ip_addr":"10.1.1.1",
    "vendor":"cisco",
    "username":"admin",
    "password":"secret"
    }

print( "\n IP: \n", net_device1["ip_addr"] )

if net_device1['vendor'].lower() == 'cisco':
    net_device1['platform'] = 'ios'
elif net_device1['vendor'].lower() == 'juniper':
    net_device1['platform'] = 'junos'


bgp_fields = {'bgp_as':"65000",'peer_as':"65555",'peer_ip':"192.168.1.1"}

print( "\n bgp_field:")
for field in bgp_fields:
    net_device1.update(bgp_fields)
    print( field, bgp_fields[field] )

print( "\n final net_device1:" )
pprint( net_device1 )




print("\nktb:\n", '-' * 80)
for key, value in net_device1.items():
    print("{key:>15} ---> {value:>15}".format(key=key, value=value))
print('-' * 80)
print()