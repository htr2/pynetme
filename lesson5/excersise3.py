#/usr/bin/env python
"""
Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following
format:
01:23:45:67:89:AB
This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
The function should have one parameter, the mac_address. It should return the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:
a:b:c:d:e:f
should be converted to:
0A:0B:0C:0D:0E:0F
Write several test cases for your function and verify it is working properly.
"""
from __future__ import print_function, unicode_literals
import re

def normalise_mac(mac_address):
    mac_address = mac_address.upper()
    normalised_mac = []
    work_mac = re.split(r"[-:.]", mac_address)
    if len(work_mac) == 3:
        for mac_parts in work_mac:
            mac_part1 = mac_parts
            if len(mac_part1) < 4:
                mac_part1 = mac_part1.zfill(4)
            normalised_mac.append(mac_part1[:2])
            normalised_mac.append(mac_part1[2:])
    elif len(work_mac) == 6:
        for mac_part1 in work_mac:
            if len(mac_part1) < 2:
                mac_part1 = mac_part1.zfill(2)
            normalised_mac.append(mac_part1)
    else:
        print("Input Error")
    return ":".join(normalised_mac)

"""
print("0000.aaaa.bbbb:",normalise_mac("0000.aaaa.bbb"))
print("00-00-aa-aa-bb-bb:",normalise_mac("00-00-aa-aa-bb-bb"))
print("a:b:c:d:e:f:",normalise_mac("a:b:c:d:e:f"))
print("1:1:1:1",normalise_mac("1:1:1:1"))
"""
# Some tests
assert "01:23:02:34:04:56" == normalise_mac('123.234.456')
assert "AA:BB:CC:DD:EE:FF" == normalise_mac('aabb.ccdd.eeff')
assert "0A:0B:0C:0D:0E:0F" == normalise_mac('a:b:c:d:e:f')
assert "01:02:0A:0B:03:44" == normalise_mac('1:2:a:b:3:44')
assert "0A:0B:0C:0D:0E:0F" == normalise_mac('a-b-c-d-e-f')
assert "01:02:0A:0B:03:44" == normalise_mac('1-2-a-b-3-44')
print("Tests passed")