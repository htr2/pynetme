#!/usr/bin/env python
from __future__ import print_function

sh_ver = """"show_version = "*0        CISCO881-SEC-K9       FTX0000038X    """
print(sh_ver)

sh_ver=sh_ver.strip()
print(sh_ver)

fields=sh_ver.split()

model= fields[3]
serial= fields[4]

#test1
vendor="cisco" in model.lower()
print("Model contains Cisco: {}".format(vendor))

#test2
type="881" in model 
print("Model contains 881: {}".format(type))


print("Serial : {}".format(serial))

