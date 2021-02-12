from scapy.all import *
import re
import tkinter as tk
from tkinter import filedialog

def show_frame(frame):
    frame.tkraise()


window=tk.Tk()
window.state('zoomed')

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

frame1=tk.Frame(window)
frame2=tk.Frame(window)


for frame in (frame1,frame2):
    frame.grid(row=0,column=0,sticky='nsew')


#Frame 1 code
frame1_title=tk.Label(frame1,text='This is frame 1',bg='red')
frame1_title.pack(fill='x')

frame1_btn=tk.Button(frame1,text='Enter',command=lambda:show_frame(frame2))
frame1_btn.pack()

#Frame 2 code
frame2_title=tk.Label(frame2,text='This is frame 2',bg='black')
frame2_title.pack(fill='x')

frame2_btn=tk.Button(frame2,text='Enter',command=lambda:show_frame(frame1))
frame2_btn.pack()

show_frame(frame1)

window.mainloop()

# def find_ip(file):
#     # file= "C:/Users/LENOVO/Desktop/log1.pcap"
#     result = ""
#     pkts = rdpcap(file)
#     #regex for source ip address
#     pattern = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')
#     lst=[] 
#     for pkt in pkts:
#         a = pkt.show(dump=True)
#         find= pattern.search(a)
#         lst.append(find[0]) 
#     # for ip in lst:
#     #     return (ip)
#     return (lst)
        


    

# def find_mac(file):
#     pkts = rdpcap(file)
#     #regex for mac address
#     pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
#     lst=[] 
#     for pkt in pkts:
#         a = pkt.show(dump=True)
#         find= pattern.search(a)
#         lst.append(find[0]) 
#     return (lst)


# def find_port(file):
#     pkts = rdpcap(file)
#     #regex for mac address
#     pattern = re.compile(r'([0-9]{2,4})')
#     lst=[] 
#     for pkt in pkts:
#         a = pkt.show(dump=True)
#         find= pattern.search(a)
#         lst.append(find[0]) 
#     print (lst)


# # file = "C:/Users/LENOVO/Desktop/log1.pcap"
# # find_ip(file)
# # find_mac(file)

# def UploadAction(event=None):
#     global filename
#     filename = filedialog.askopenfilename()
#     return filename

# def main():
#     root = tk.Tk()
#     button = tk.Button(root, text='Open', command=UploadAction)
#     button.pack()
#     result = tk.Label(root, text='')
    
#     ip_btn = tk.Button(root, text='Find IPs')
#     ip_btn.config(command=lambda: result.config(text=("\n\n".join(find_ip(filename)))))
#     ip_btn.pack()
#     result.config(text="") 
#     ip_btn = tk.Button(root, text='Find mac')
#     ip_btn.config(command=lambda: result.config(text=("\n".join(find_mac(filename)))))
#     ip_btn.pack() 


#     result.pack(padx = 5, pady = 25)
#     root.mainloop()


# # find_ip(file)
# # find_mac(file)
# # find_port(file)


# if __name__ == "__main__":
#     main()

