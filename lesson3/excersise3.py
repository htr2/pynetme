#!/usr/bin/env python
''''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
'''

from __future__ import unicode_literals, print_function
from pprint import pprint

with open("lesson3/show_lldp_neighbor.txt") as f:
    f_str = f.read()

system_name = ""
port_id = ""
i=0

for line in f_str.splitlines():
    line_fields = line.split(":")
    #print("line:",i)
    i=i+1
    for result_tuple in enumerate(line_fields):
        #print("line_fields:",line_fields)
        if result_tuple[1] == "System Name":
            system_name = line_fields[1]
        if result_tuple[1] == "Port id":
            port_id = line_fields[1]
    if system_name and port_id:
        print("system name:", system_name, "port id:", port_id, "exiting")
        break
            

        
