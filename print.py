from scapy.all import *
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk

def show_frame(frame):
    frame.tkraise()


window=tk.Tk()
# Adjust size  
window.title('PythonProject')
#window.iconbitmap('PythonProject\PythonProject\Images\python.png')
window.geometry("500x300")
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

load=Image.open('C:/Users/Lindë Imeri/Desktop/PythonProject/PythonProject/Images/python.png')
render=ImageTk.PhotoImage(load)
img=Label(window,image=render)
img.place(x=0,y=0)

text_label=Label(window,text="Read your log files",bd='8',bg='#42ddf5',activebackground='#42ddf5')
text_label.config(font=("Arial", 12),)
text_label.place(x=20,y=50)

frame2=tk.Frame(window)

b1=Button(window,text="Start",bd=0,bg='#42ddf5',activebackground='#42ddf5',width='15',command=lambda:show_frame(frame2))
b1.config(font=("Arial", 12),)
b1.place(x=20,y=200)


 frame1=tk.Frame(window)



# for frame in (frame1,frame2):
#     frame.grid(row=0,column=0,sticky='nsew')


# #Frame 1 code

# frame1_btn=tk.Button(frame1,text='Get Started',command=lambda:show_frame(frame2),bg='blue')
# frame1_btn.grid(row=1,column=1,pady=10, padx=30)
# frame1_btn.pack()

# frame1_image=tk.Label(frame1,image=img,bd=0)
# frame1_image.place(x=0,y=0,relwidth=1,relheight=1)
# frame1_image.pack()


#Frame 2 code
# frame2_title=tk.Label(frame2,text='This is frame 2',bg='black')
# frame2_title.pack(fill='x')

# frame2_btn=tk.Button(frame2,text='Enter',command=lambda:show_frame(frame1))
# frame2_btn.pack()





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


def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    return filename

def on_enter(e):
    e.widget['background'] = '#849299'

def on_leave(e):
    e.widget['background'] = '#3e6678'

def main():
    # root = tk.Tk(className=' Regex Application')
    # root.geometry("500x300")
    button = tk.Button(frame2, text='Select log file', command=UploadAction, bg='#3e6678', fg='white')
    button.grid(row=1,column=1,pady=10, padx=30)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    result = tk.Label(frame2, text='')
    
    ip_btn = tk.Button(frame2, text='Find Source IP Addresses',  bg='#3e6678', fg='white')
    ip_btn.config(command=lambda: result.config(text=(" \n\n".join(find_ip(filename)))))
    ip_btn.grid(row=3,column=1, padx=30)
    ip_btn.bind("<Enter>", on_enter)
    ip_btn.bind("<Leave>", on_leave)
    result.config(text="") 



    mac_btn = tk.Button(frame2, text='Find Source Mac Addresses',  bg='#3e6678', fg='white')
    mac_btn.config(command=lambda: result.config(text=("\n\n".join(find_mac(filename)))))
    mac_btn.grid(row=3,pady=10, column=3, padx=20)
    mac_btn.bind("<Enter>", on_enter)
    mac_btn.bind("<Leave>", on_leave)

    result_label = tk.Label(frame2, text='Result: ', bg='#3e6678',fg='white')
    result_label.grid(row=4,column=2)
    result.grid(row=5,column=2)
    # root.mainloop()

show_frame(frame2)



if __name__ == "__main__":
    main()

window.mainloop()