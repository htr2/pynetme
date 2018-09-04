#!/usr/bin/env python
from __future__ import print_function

str = """"
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"    
"""

str=str.strip()
print(str)

a,b,c=str.split("\n")

afields = a.split()
bfields = b.split()
cfields = c.split()

print("_" *20, "_" *20)
print("{:>20} {:>20}".format("IP Addr", "MAC Addr"))
print("_" *20, "_" *20)

print("{:>20} {:>20}".format(afields[3], afields[5]))
print("{:>20} {:>20}".format(bfields[3], bfields[5]))
print("{:>20} {:>20}".format(cfields[3], cfields[5]))
#print(" : {:^20}".format(fields))


