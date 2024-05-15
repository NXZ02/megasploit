
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
	pip install pygame --break-system-packages
	pip install tk --break-system-packages
	pip install customtkinter --break-system-packages
	pip install pillow --break-system-packages
	sudo apt install python3-dev -y 
	sudo apt install python3-pil python3-pil.imagetk
elif [ $tk == 2 ]; 
	then
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

