#!/usr/bin/env python
"""
Read the 'show_ipv6_intf.txt' file.
From this file use Python regular expressions to extract the two IPv6 addresses.
The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of
the literal characters in the IPv6 address.
From this, create a list of IPv6 addresses that includes only the above two addresses.
Print this list to the screen.
"""
from __future__ import unicode_literals, print_function
import re

with open("lesson4/show_ip_int.txt") as f:
    f_str = f.read()


#se re.DOTALL to have .* span newlines
match = re.search(r"IPv6 address:\s+(.*).....[VALID].\s+(.*)IPv6 subnet:", f_str, flags=re.DOTALL)

ipv6_list = [match.group(1).strip(),match.group(2).strip()]
print("IPv6 addresses are:", ipv6_list)




