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
        if find[0] not in lst: 
            lst.append(find[0]) 
    return (lst)
        

def find_mac(file):
    pkts = rdpcap(file)
    #regex for mac address
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    lst=[] 
    for pkt in pkts:
        a = pkt.show(dump=True)
        find= pattern.search(a)
        if find[0] not in lst: 
            lst.append(find[0])  
    return (lst)



def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    return filename

def on_enter(e):
    e.widget['background'] = '#849299'

def on_leave(e):
    e.widget['background'] = '#3e6678'

def main():
    root = tk.Tk(className=' Regex Application')
    root.geometry("500x300")
    button = tk.Button(root, text='Select log file', command=UploadAction, bg='#3e6678', fg='white')
    button.grid(row=1,column=1,pady=10, padx=30)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    result = tk.Label(root, text='')
    
    ip_btn = tk.Button(root, text='Find Source IP Addresses',  bg='#3e6678', fg='white')
    ip_btn.config(command=lambda: result.config(text=(" \n\n".join(find_ip(filename)))))
    ip_btn.grid(row=3,column=1, padx=30)
    ip_btn.bind("<Enter>", on_enter)
    ip_btn.bind("<Leave>", on_leave)
    result.config(text="") 



    mac_btn = tk.Button(root, text='Find Source Mac Addresses',  bg='#3e6678', fg='white')
    mac_btn.config(command=lambda: result.config(text=("\n\n".join(find_mac(filename)))))
    mac_btn.grid(row=3,pady=10, column=3, padx=20)
    mac_btn.bind("<Enter>", on_enter)
    mac_btn.bind("<Leave>", on_leave)

    result_label = tk.Label(root, text='Result: ', bg='#3e6678',fg='white')
    result_label.grid(row=4,column=2)
    result.grid(row=5,column=2)
    root.mainloop()



if __name__ == "__main__":
    main()