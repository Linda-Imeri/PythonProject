from scapy.all import *
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import os

def show_frame(frame):
    frame.tkraise()


window=tk.Tk()
# Adjust size  
window.title('Regex Application')
window.iconbitmap('Images/python.png')
window.geometry("490x300")
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.resizable(width=False, height=False)
frame1=tk.Frame(window)
frame2=tk.Frame(window)

for frame in (frame1,frame2):
    frame.grid(row=0,column=0,sticky='nsew')

load=Image.open('Images/python.png')
render=ImageTk.PhotoImage(load)
img=Label(frame1,image=render)
img1=Label(frame2,image=render)
img.place(x=0,y=0)
img1.place(x=0,y=0)

text_label=Label(frame1,text="Read your log files",bd='8',bg='#00233B',fg='white',width='15')
text_label.config(font=("Arial", 12),)
text_label.place(x=20,y=50)




#Frame 1 code

frame1_btn=tk.Button(frame1,text='Start',command=lambda:show_frame(frame2),bd='1',bg='#00233B', fg='white',activebackground='#00233B',width='10')
frame1_btn.config(font=("Arial", 12),)
frame1_btn.place(x=20,y=180)



def find_ip(file):

    result = ""
    file_extension = os.path.splitext(file)[1]
    if(file_extension==".txt"):

        # opening and reading the file  
        with open(file) as fh: 
            fstring = fh.readlines() 
        
        # declaring the regex pattern for IP addresses 
        pattern = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')
        
        # initializing the list object 
        lst=[] 
        
        # extracting the IP addresses 
        for line in fstring: 
            find = pattern.search(line)
            if find[0] not in lst:
                lst.append(find[0]) 
        
        # displaying the extracted IP adresses 
        return(lst) 

    else:
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
    file_extension = os.path.splitext(file)[1]
    if(file_extension==".txt"):

        # opening and reading the file  
        with open(file) as fh: 
            fstring = fh.readlines() 
        
        # declaring the regex pattern for IP addresses 
        pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
        
        # initializing the list object 
        lst=[] 
        
        # extracting the IP addresses 
        for line in fstring: 
             find = pattern.search(line)
             if find[0] not in lst:
                lst.append(find[0])
        
        # displaying the extracted IP adresses 
        return(lst) 

    else:   
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
    
    e.widget['background'] = '#0098EB'

def on_leave(e):
    e.widget['background'] = '#00233B'

def main():
    # root = tk.Tk(className=' Regex Application')
    # root.geometry("500x300")
    button = tk.Button(frame2, text='Select log file', command=UploadAction, bg='#00233B', fg='white')
    button.grid(row=1,column=2,pady=10, padx=30)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    result = tk.Label(frame2, text='Select a file to show results!')
    
    ip_btn = tk.Button(frame2, text='Find Source IP Addresses',  bg='#00233B', fg='white')
    ip_btn.config(command=lambda: result.config(text=("\n\n".join(find_ip(filename)))))
    ip_btn.grid(row=3,column=1, padx=15)
    ip_btn.bind("<Enter>", on_enter)
    ip_btn.bind("<Leave>", on_leave)
    #result.config(text="") 



    mac_btn = tk.Button(frame2, text='Find Source Mac Addresses',  bg='#00233B', fg='white')
    mac_btn.config(command=lambda: result.config(text=("\n\n".join(find_mac(filename)))))
    mac_btn.grid(row=3,pady=10, column=3, padx=15)
    mac_btn.bind("<Enter>", on_enter)
    mac_btn.bind("<Leave>", on_leave)

    result_label = tk.Label(frame2, text='Result: ', bg='#00233B',fg='white')
    result_label.grid(row=4,column=2)
    result.grid(row=5,column=2)
    # root.mainloop()

    show_frame(frame1)
    window.mainloop() 



if __name__ == "__main__":
    main()

