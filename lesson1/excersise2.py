#!/usr/bin/env python
from __future__ import print_function

S
try:
	#PY2
	ip_addr = raw_input("PY2 Please enter an IP address: ")
except NameError:
    # PY3
    ip_addr = input("PY3 Please enter an IP address: ")

print (ip_addr)

octets = ip_addr.split(".")
print()
print()
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])),
                                        bin(int(octets[2])), bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])),
                                        hex(int(octets[2])), hex(int(octets[3]))))
print("-" * 60)
print()