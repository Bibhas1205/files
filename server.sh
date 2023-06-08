if [ $# -eq 1 ]
then
	sudo /opt/lampp/xampp $1
	clear
	echo "Your Local server (127.0.0.1/localhost) has $1ed"
 	echo "Your server's path : /opt/lampp/htdocs/"
else
	clear
	echo "Please Enter start or stop parameter"
fi



