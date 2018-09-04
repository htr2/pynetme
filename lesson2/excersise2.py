""""Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list."""

ip_list=["192.168.1.1","172.16.1.1","10.1.1.1","2.2.2.2","224.224.224.224"]
print("Baselist:","\n",ip_list,"\n")

ip_list.append("192.168.255.255")
ip_list.append("172.16.255.255")
print("Baselist appended:","\n",ip_list,"\n")


ip_list.extend(["192.168.255.255","172.16.255.255"])
print("Baselist appended extended:","\n",ip_list,"\n")

ip_list = ip_list + ["10.255.255.255","2.255.255.255"]
print("Baselist appended extended concatenated:","\n",ip_list,"\n")

print("first:","\n", ip_list[0], "\n")
print("last:","\n", ip_list[-1], "\n")

ip_list.pop(0)
ip_list.pop(-1)

print("first after pop:","\n", ip_list[0], "\n")
print("last after pop:","\n", ip_list[-1], "\n")

ip_list[0] = "2.2.2.2"
last_ip = ip_list.pop()

print("new first:","\n", ip_list[0], "\n")
print("last:","\n", last_ip, "\n")

print("final lsit:","\n",ip_list,"\n")
