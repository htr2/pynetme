#!/usr/bin/env python
""""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""
from __future__ import unicode_literals, print_function
from pprint import pprint

with open("lesson3/show_vlan.txt") as f:
    f_str = f.read()

result_list = []

for line in f_str.splitlines():
    if "----" in line:
        continue
    elif "VLAN" in line:
        continue
    elif "Et" in line:
        continue
    fields = line.split()
    #print("fields:",fields )
    a=fields[0]
    b=fields[1]
    #print("a:",a)
    #print("b:",b)
    result_list.append((a,b))

pprint( result_list )