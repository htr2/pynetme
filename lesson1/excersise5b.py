#!/usr/bin/env python
from __future__ import print_function


result_list = []

with open("file.txt") as f:
	str = f.read()

str = str.strip()

for line in str.splitlines():
	fields = line.split()
	result1 = fields[3]
	result2 = fields[5]
	result_list.append((result1,result2))
	
#print(result1)
print(result_list)
print("{:^15}{:^15}".format(result1, result2))