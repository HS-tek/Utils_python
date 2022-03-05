import scapy.all as scapy
import re

#For wired connection, enter on terminal ---> ipconfig getifaddr en1
#For Wi-Fi connection, enter on terminal ---> ipconfig getifaddr en0
#For Public ip, enter on terminal ----------> curl ifconfig.me
#Expression Pattern to recognise IPv4 addresses
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

#Get adress range
while True:
    ip_add_range_entered = input("\nPlease enter ip address and range")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break

arp_result = scapy.arping(ip_add_range_entered)
