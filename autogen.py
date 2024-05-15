from tkinter import *
from customtkinter import *
import tkinter.messagebox
from pygame import mixer
mixer.init()

def ERR():
	mixer.music.load("error.mp3")
	mixer.music.play()
mixer.init()
def PLAY():
	mixer.music.load("click_a.wav")
	mixer.music.play()

wine = CTk()
wine.resizable(width=False, height=False)
wine.geometry("300x500")
wine.title("Config auto script")
set_appearance_mode("light")
def window():
	PLAY()
	os.system("xdg-open gen_windows.rc")
def linux():
	PLAY()
	os.system("xdg-open gen_linux.rc")
def android():
	PLAY()
	os.system("xdg-open gen_android.rc")

def autorate():
	if READ_WINDOWS.get() + READ_LINUX.get() + READ_ANDROID.get() != 1:
		ERR()
		tkinter.messagebox.showerror("Message ERROR","Please select only 1 option.")
	if READ_WINDOWS.get() == 1:
		PLAY()
		wine.destroy()
		os.system("msfconsole -q -r gen_windows.rc")
	if READ_LINUX.get() == 1:
		PLAY()
		wine.destroy()
		os.system("msfconsole -q -r gen_linux.rc")
	if READ_ANDROID.get() == 1:
		PLAY()
		wine.destroy()
		os.system("msfconsole -q -r gen_android.rc")




READ_WINDOWS = IntVar()
READ_LINUX = IntVar()
READ_ANDROID = IntVar()



CTkLabel(wine , text="Config autogen",text_color="#C850C0") .place(relx=0.3, rely= 0.1)
CTkButton(wine , text="Windows",command=window,border_color="#FFCC70",fg_color="red",border_width=2, hover_color="green") .place(relx=0.2 , rely=0.2)
CTkButton(wine , text="Linux",command=linux,border_color="#FFCC70",fg_color="red",border_width=2, hover_color="green") .place(relx=0.2 , rely=0.3)
CTkButton(wine , text="Android",command=android,border_color="#FFCC70",fg_color="red",border_width=2, hover_color="green") .place(relx=0.2 , rely=0.4)
CTkLabel(wine , text="autogen",text_color="red") .place(relx=0.3, rely= 0.5)
CTkCheckBox(master=wine, text="Windows",fg_color="red",corner_radius=36, onvalue=1,offvalue=0,variable=READ_WINDOWS) .place(relx=0.5, rely=0.6 ,anchor="center")
CTkCheckBox(master=wine, text="Linux",fg_color="red",corner_radius=36, onvalue=1,offvalue=0,variable=READ_LINUX) .place(relx=0.5, rely=0.7 ,anchor="center")
CTkCheckBox(master=wine, text="Android",fg_color="red",corner_radius=36, onvalue=1,offvalue=0,variable=READ_ANDROID) .place(relx=0.5, rely=0.8 ,anchor="center")
CTkButton(master=wine,text="BUILD",border_color="#FFCC70",fg_color="red",border_width=2, hover_color="green",command=autorate) .place(relx=0.5, rely=0.9, anchor="center")
wine.mainloop()
