#!/usr/bin/env python
from __future__ import print_function

#2001:cdba:0000:0000:0000:0000:3257:9652
#:::::::9652

ipvsix_addr_one=":::::::9652"
IPVSIX_ADDR_TWO=":::::::9652"
ipv6_addr3="2001:::::::"

test1=ipvsix_addr_one == IPVSIX_ADDR_TWO
test2=ipvsix_addr_one == ipv6_addr3

print(test1)
print(test2)