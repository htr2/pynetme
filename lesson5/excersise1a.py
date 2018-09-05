#!/usr/bin/env python
"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.
Call this ssh_conn function using entirely positional arguments.
Call this ssh_conn function using entirely named arguments.
Call this ssh_conn function using a mix of positional and named arguments.
"""
from __future__ import print_function, unicode_literals


def ssh_conn(ip_add, username, password):
    print("ip_add:",ip_add)
    print("username:",username)
    print("password:",password)

print()
print("positional arg:")
ssh_conn("172.16.1.1","peter","secret")
print()

print("named arg:")
ssh_conn(password="secret",ip_add="172.16.1.1",username="peter")
print()

print("mix arg:")
ssh_conn("172.16.1.1",password="secret",username="peter")
print()
