from scapy.all import *
import re
from collections import Counter

pkts = rdpcap("C:/Users/LENOVO/Desktop/log1.pcap")
# print (len(pkts))

#regex for source ip address
pattern = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')
#regex for mac address
#pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
lst=[] 
for pkt in pkts:
    a = pkt.show(dump=True)
    find= pattern.search(a)
    lst.append(find[0]) 
print (lst)


