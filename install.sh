G="$(printf '\033[1;32m')"
Y="$(printf '\033[1;33m')"
W="$(printf '\033[1;37m')"
C="$(printf '\033[1;36m')"
R="$(printf '\033[1;31m')"


head(){
	echo ${Y}
	echo "[1] debian"
	echo "[2] arch "
	echo
}

head2(){
	echo  ${Y}
	echo -e "[1] = fix system break"
	echo 
	echo -e "[2] = if option 1 error install you choose option2"	
	echo  
} 
apt() {
    if ! which apt  > /dev/null; then
    	echo
    else
    	sudo apt install -y figlet
 
fi
} 
arch() {
    if ! which pacman   > /dev/null; then
    echo
    else
    	sudo pacman -S  --noconfirm figlet
 
fi
}

apt
arch
clear 
figlet ROOT 
echo 

head
echo ${C}
read -p "choose : " tk 

if [ $tk == 1 ];
then
	clear
	figlet OPTIONS
	head2
	echo ${C}
	read -p "choose option :   " str
	if [ $str == 1 ]; then
	# system break fix 
	sudo apt install python3-pip -y 
	pip install pygame --break-system-packages
	pip install tk --break-system-packages
	pip install customtkinter --break-system-packages
	pip install pillow --break-system-packages
	sudo apt install python3-dev -y 
	sudo apt install python3-pil python3-pil.imagetk -y 

	elif [ $str == 2 ]; then
	# option 1 error 
	 sudo apt install python3-pip -y 
	 pip install pygame 
	 pip install tk 
	 pip install customtkinter 
	 pip install pillow 
	 sudo apt install python3-dev -y 
	 sudo apt install python3-pil python3-pil.imagetk -y 
 	fi 
		

elif [ $tk == 2 ]; 
	then
		echo ${G}
		clear
		figlet OPTIONS
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

