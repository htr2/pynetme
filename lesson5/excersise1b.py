#!/usr/bin/env python
"""
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with
a default value of 'cisco_ios'. Print all four of the function variables out as part of the
function's execution.
Call the 'ssh_conn2' function both with and without specifying the device_type
Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
the **kwargs technique.
"""
from __future__ import print_function, unicode_literals
from __future__ import print_function, unicode_literals


def ssh_conn2(ip_add, username, password,device_type="cisco"):
    print("ip_add:",ip_add)
    print("username:",username)
    print("password:",password)
    print("device_type:",device_type)

print()
print("positional arg:")
ssh_conn2("172.16.1.1","peter","secret","juniper")
print()

print("named arg:")
ssh_conn2(device_type="orion",password="secret",ip_add="172.16.1.1",username="peter")
print()

print("mix arg:")
ssh_conn2("172.16.1.1",password="secret",username="peter")
print()

dic =  {
        "device_type":"F5",
        "password":"secret",
        "ip_add":"172.16.1.1",
        "username":"peter"
        }

print("dic arg:")
ssh_conn2(**dic)
print()

