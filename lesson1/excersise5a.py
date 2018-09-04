#!/usr/bin/env python
from __future__ import print_function

str = """"
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"    
"""

str = str.strip()

result_list = []

#with open("file.txt") as f:
#str = f.read()

for line in str.splitlines():
	fields = line.split()
	result1 = fields[3]
	result2 = fields[5]
	result_list.append((result1,result2))
	
print(result1)
#print(result_list)
print(result_list[0])