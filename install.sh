
head(){
	echo "[1] debian"
	echo "[2] arch "
}

clear 
figlet ROOT 
echo 

head

read -p "choose : " tk 

if [ $tk == 1 ];
then
 	sudo apt install python3-pip -y 
	pip install pygame --break-system-packages
	pip install tk --break-system-packages
	pip install customtkinter --break-system-packages
	pip install pillow --break-system-packages
	sudo apt install python3-dev -y 
	sudo apt install python3-pil python3-pil.imagetk -y 
 # system break fix remove #
 	 #sudo apt install python3-pip -y 
	 #pip install pygame 
	 #pip install tk 
	 #pip install customtkinter 
	 #pip install pillow 
	 #sudo apt install python3-dev -y 
	 #sudo apt install python3-pil python3-pil.imagetk -y 
 
elif [ $tk == 2 ]; 
	then
 		sudo pacman -S python-pip --noconfirm
		sudo pacman -S tk --noconfirm
		pip install tk --break-system-packages
		pip install customtkinter --break-system-packages
		pip install pillow --break-system-packages
		pip install pygame --break-system-packages
else
clear
echo -e "error"
sleep 1
./install.sh
fi

