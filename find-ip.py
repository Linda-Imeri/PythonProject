from scapy.all import *
import re
import tkinter as tk
from tkinter import filedialog

def find_ip(file):
    # file= "C:/Users/LENOVO/Desktop/log1.pcap"
    result = ""
    pkts = rdpcap(file)
    #regex for source ip address
    pattern = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')
    lst=[] 
    for pkt in pkts:
        a = pkt.show(dump=True)
        find= pattern.search(a)
        lst.append(find[0]) 
    # for ip in lst:
    #     return (ip)
    return (lst)
        


    

def find_mac(file):
    pkts = rdpcap(file)
    #regex for mac address
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    lst=[] 
    for pkt in pkts:
        a = pkt.show(dump=True)
        find= pattern.search(a)
        lst.append(find[0]) 
    return (lst)


def find_port(file):
    pkts = rdpcap(file)
    #regex for mac address
    pattern = re.compile(r'([0-9]{2,4})')
    lst=[] 
    for pkt in pkts:
        a = pkt.show(dump=True)
        find= pattern.search(a)
        lst.append(find[0]) 
    print (lst)


# file = "C:/Users/LENOVO/Desktop/log1.pcap"
# find_ip(file)
# find_mac(file)

def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    return filename

def main():
    root = tk.Tk()
    button = tk.Button(root, text='Open', command=UploadAction)
    button.pack()
    result = tk.Label(root, text='')
    
    ip_btn = tk.Button(root, text='Find IPs:')
    ip_btn.config(command=lambda: result.config(text=("\n\n".join(find_ip(filename)))))
    ip_btn.pack()
    result.config(text="") 
    ip_btn = tk.Button(root, text='Find mac:')
    ip_btn.config(command=lambda: result.config(text=("\n".join(find_mac(filename)))))
    ip_btn.pack() 


    result.pack(padx = 5, pady = 25)
    root.mainloop()


# find_ip(file)
# find_mac(file)
# find_port(file)


if __name__ == "__main__":
    main()
