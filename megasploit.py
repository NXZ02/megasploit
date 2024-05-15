from customtkinter import *
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory
import os
import BUILD
import tkinter.messagebox
from PIL import Image , ImageTk
from PIL import *
from pygame import mixer

mixer.init()
def PLAY():
	mixer.music.load("click_a.wav")
	mixer.music.play()
def ERR():
	mixer.music.load("error.mp3")
	mixer.music.play()

def pas():
	mixer.music.load("click_b2.wav")
	mixer.music.play()

window = CTk()
window.geometry("900x500")
window.title("Megasploit")
window.resizable(width=False, height=False)
set_appearance_mode("dark")
def EXIT_PROGRAM():
	PLAY()
	window.destroy()

mylist = Menu()
window.config(menu=mylist)


img = PhotoImage(file="7.png")
img = img.zoom(15) #with 250, I ended up running out of memory
img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320
panel = Label(window, image = img, bd=0) .place(x=70, y= 190)



def Build():
	PLAY()
	SAVE = askdirectory()
	NAME = str1.get()
	IP = str2.get()
	PORT = str3.get()
	
	if READ_WINDOWS.get() + READ_LINUX.get() + READ_ANDROID.get() != 1:
		ERR()
		tkinter.messagebox.showerror("Message ERROR","Please select only 1 option.")

	elif READ_WINDOWS.get() == 1:
		BUILD.create_windows(IP , PORT , NAME , SAVE)
		pas()
		tkinter.messagebox.showinfo("Message ","create payload compleat !")

	elif READ_LINUX.get() == 1:
		BUILD.create_linux(IP , PORT , NAME , SAVE)
		pas()
		tkinter.messagebox.showinfo("Message ","create payload compleat !")

	elif READ_ANDROID.get() == 1:
		BUILD.create_android(IP , PORT , NAME , SAVE)
		pas()
		tkinter.messagebox.showinfo("Message ","create payload compleat !")
	


def ABOUT():
	PLAY()



	os.system("python3 call.py &")

def gen():
	PLAY()
	os.system("python3 autogen.py &")



mylist.add_command(label="Config autorun",command=gen)
mylist.add_command(label="About",command=ABOUT)

mylist.add_command(label="Exit",command=EXIT_PROGRAM)
str1 = StringVar()
str2 = StringVar()
str3 = StringVar()
READ_WINDOWS = IntVar()
READ_LINUX = IntVar()
READ_ANDROID = IntVar()

#SAVE_PATH = StringVar()




CTkLabel(window,text="PAYLOAD_NAME",font=("Arial",16),text_color="#C850C0").place(x=60,y=45) 
CTkEntry(master=window,textvariable=str1) .place(x=60,y=80)

CTkLabel(window,text="IP ",font=("Arial",16),text_color="#C850C0").pack(padx=0,pady=50)
entry = CTkEntry(master=window,textvariable=str2, placeholder_text="Start typing...") .place(x=380,y=80)

CTkLabel(window,text="PORT",font=("Arial",16),text_color="#C850C0").place(x=700,y=45)
CTkEntry(master=window,textvariable=str3) .place(x=700,y=80)



CTkLabel(window,text="PAYLOAD LIST",font=("Arial",16),text_color="green").place(relx=0.5, rely=0.3,anchor="center")
CTkCheckBox(master=window, text="Windows",fg_color="#C850C0",corner_radius=36,variable=READ_WINDOWS, onvalue=1,offvalue=0) .place(relx=0.5, rely=0.4 ,anchor="center")
CTkCheckBox(master=window, text="Linux",fg_color="#C850C0",corner_radius=36,variable=READ_LINUX, onvalue=1,offvalue=0) .place(relx=0.5, rely=0.5 ,anchor="center")
CTkCheckBox(master=window, text="Android",fg_color="#C850C0",corner_radius=36,variable=READ_ANDROID, onvalue=1,offvalue=0) .place(relx=0.5, rely=0.6 ,anchor="center")

#CTkButton(master=window,text="Choose Folder",border_color="#FFCC70",fg_color="#4158D0",border_width=2, hover_color="green",command=check) .place(relx=0.5, rely=0.7, anchor="center")
CTkButton(master=window,text="BUILD",border_color="#FFCC70",fg_color="#4158D0",border_width=2, hover_color="green",command=Build) .place(relx=0.5, rely=0.8, anchor="center")




window.mainloop()