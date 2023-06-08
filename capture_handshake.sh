if [ $# -ne 2 ]
then
echo "Please Enter BSSID CHANNEL_ID"
else
sudo airodump-ng -c $2 --bssid $1 --write newcapture wlan0
fi
