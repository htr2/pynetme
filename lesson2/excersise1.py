#!/usr/bin/env python
from __future__ import print_function
from __future__ import division


banner = "_" * 120

f = open("show_version.txt")
sh_ver = f.read()
f.close()

print()
print(banner)
print(type(sh_ver),":")
print(banner)
print(sh_ver)
print(banner)
print()


with open("show_version.txt") as f:
 sh_ver = f.readlines()

print() 
print(banner)
print(type(sh_ver),":")
print(banner)
print(sh_ver)
print(banner)
print() 

