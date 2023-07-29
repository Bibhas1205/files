if [ $# -ne 2 ]
then
	echo "You must give 2 arguments <network_interface> <monitor/mannage>"
else
	if [ $2 = "monitor" ]
	then
		ifconfig $1 down
		iwconfig $1 mode monitor
		ifconfig $1 up
		airodump-ng $1
	elif [ $2 = "mannage" ]
	then
		ifconfig $1 down
		iwconfig $1 mode mannage
		ifconfig $1 up
	else
		echo "You choose a wrong argument please choose right"
	fi
fi
