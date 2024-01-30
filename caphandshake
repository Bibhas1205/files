if [ $# -ne 3 ]
then
echo "Please Enter <network_interface> <BSSID> <CHANNEL_ID>"
else
sudo airodump-ng -c $3 --bssid $2 --write newcapture $1
fi
