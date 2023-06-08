from time import sleep
from os import system
system("python3 /home/kali/Downloads/torghost/torghost.py -s")
while True:
	sleep(20)
	system("python3 /home/kali/Downloads/torghost/torghost.py -r")
