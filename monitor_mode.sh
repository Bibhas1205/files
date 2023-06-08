if [ $# -ne 1 ]
then
	echo "You must give a argument monitor/mannage"
else
	if [ $1 = "monitor" ]
	then
		ifconfig wlan0 down
		iwconfig wlan0 mode monitor
		ifconfig wlan0 up
		airodump-ng wlan0
	elif [ $1 = "mannage" ]
	then
		ifconfig wlan0 down
		iwconfig wlan0 mode mannage
		ifconfig wlan0 up
	else
		echo "You choose a wrong argument please choose right"
	fi
fi
