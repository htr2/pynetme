#/usr/bin/env python
"""
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement
outside of your function (i.e. where you have your function calls).
Inside of pdb, experiment with:
1. Listing your code.
2. Using 'next' and 'step' to walk through your code. Make sure you understand the difference
   between the two.
3. Experiment with 'up' and 'down' to move up and down the code stack.
4. Use p <variable> to look at a variable.
5. Set a breakpoint and run your code to the breakpoint.
6. Use '!command' to change a variable (for example !new_mac = [])
"""
from __future__ import print_function, unicode_literals
import re
import pdb

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
    #pdb.set_trace()
    return ":".join(normalised_mac)

"""
print("0000.aaaa.bbbb:",normalise_mac("0000.aaaa.bbb"))
print("00-00-aa-aa-bb-bb:",normalise_mac("00-00-aa-aa-bb-bb"))
print("a:b:c:d:e:f:",normalise_mac("a:b:c:d:e:f"))
print("1:1:1:1",normalise_mac("1:1:1:1"))
"""
# Some tests
assert ("01:23:02:34:04:56" == normalise_mac('123.234.456')),"Mismatch"
assert ("AA:BB:CC:DD:EE:FF" == normalise_mac('aabb.ccdd.eeff')),"Mismatch"
assert ("0A:0B:0C:0D:0E:0F" == normalise_mac('a:b:c:d:e:f')),"Mismatch"
assert ("01:02:0A:0B:03:44" == normalise_mac('1:2:a:b:3:44')),"Mismatch"
assert ("0A:0B:0C:0D:0E:0F" == normalise_mac('a-b-c-d-e-f')),"Mismatch"
assert ("01:02:0A:0B:03:44" == normalise_mac('1-2-a-b-3-44')),"Mismatch"
print("Tests passed")
