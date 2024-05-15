import os
from tkinter import *
from PIL import *
from PIL import Image , ImageTk
from customtkinter import *
from pygame import mixer
import time
mixer.init()

def sound_click():
	mixer.music.load("click_a.wav")
	mixer.music.play()

def EXIT_ZERO():
	sound_click()
	time.sleep(0.01)
	gTK.destroy()

#def RUNB():
gTK = Tk()
gTK.geometry("450x450")
gTK.resizable(width=False, height=False)
gTK.title("About")
backgourd = PhotoImage(file="bg.png")
Label(gTK, image=backgourd) .place(x=0)





	
LOGO = Image.open("7.png")
New = LOGO.resize((200, 200))
photo=ImageTk.PhotoImage(New)
Label(master=gTK, image=photo,bd=0) .place(x=100)
Label(gTK, text="Hacker Tools",bg="green",fg="black") .place(relx=0.7, rely=0.1)
Label(gTK, text="metasploit",bg="green",fg="black") .place(relx=0.7, rely=0.2)
Label(gTK, text="Version0.1",bg="green",fg="black") .place(relx=0.7, rely=0.3)
Label(gTK, text="Create by ",bg="green",fg="black") .place(relx=0, rely=0.1)
Label(gTK, text="NXZ02",bg="green",fg="black") .place(relx=0, rely=0.2)
Label(gTK, text="Tools",bg="green",fg="black") .place(relx=0.4, rely=0.5)
Label(gTK, text="Python, lib ( tkinter, customtkinter, PIL metasploit) ",bg="green",fg="black") .place(relx=0.1, rely=0.6)
Label(gTK, text="For Linux Debian/Arch Linux/Redhat",bg="green",fg="black") .place(relx=0.1, rely=0.7)
CTkButton(master=gTK,text="Quit",border_color="#FFCC70",fg_color="red",border_width=2, hover_color="black",command=EXIT_ZERO) .place(relx=0.3 ,rely=0.5)

gTK.mainloop()

