#!/usr/bin/env python
""""
Create three separate lists of IP addresses. The first list should be the IP addresses for the
Houston data center routers and should have over ten IP addresses in it including some duplicate IP
addresses.
The second list should be the Atlanta data center routers and should have at least eight IP
addresses including some that overlap with the Houston data center.
The third list should be the Chicago data center routers and should have at least eight IP
addresses. The Chicago IP addresses have some overlap with the IP addresses in both Houston
and in Atlanta
Convert each of these three lists to a set.
Using set operations, find the IP addresses that are duplicated between Houston and Atlanta.
Using set operations, find the IP addresses that are duplicated in all three sites.
Using set operations, find the IP addresses that are entirely unique in Chicago.
"""
from __future__ import unicode_literals, print_function

houdc_iplist = ["10.1.1.1","172.16.1.1","192.168.1.1","8.8.8.8","2.2.2.2","1.1.1.1","10.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4"]
atldc_iplist = ["172.16.1.1","3.3.3.3","5.5.5.5","6.6.6.6","7.7.7.7","9.9.9.9","10.2.2.2","192.168.2.2"]
chidc_iplist = ["8.8.8.8","1.1.1.1","5.5.5.5","10.2.2.2","10.3.3.3","172.16.3.3","192.168.3.3","3.3.3.3"]

houdc_iplist = set(houdc_iplist)
atldc_iplist = set(atldc_iplist)
chidc_iplist = set(chidc_iplist)

print()
print( "Houston:", houdc_iplist)
print( "Atlanta:", atldc_iplist)
print( "Chicago:", chidc_iplist)

print()
print("Duplicate IPs at Houston and Atlanta sites:\n{}".format(houdc_iplist & atldc_iplist))
print()
print("Duplicate IPs at 3 sites:\n{}".format(houdc_iplist & atldc_iplist & chidc_iplist))
print()
print("Unique IPs in Chicago:\n{}".format(chidc_iplist.difference(houdc_iplist).difference(atldc_iplist)))