import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import json
from gtts import gTTS
import os

#Provide your IBM Watson Device Credentials
organization = "c6kfqv"
deviceType = "iotdevice"
deviceId = "1001"
authMethod = "token"
authToken = "1234567890"


# Initialize the device client.
T=0
H=0
notice=" "
def myCommandCallback(cmd):
        print("Notice %s" % cmd.data['command'])
        notice=cmd.data['command']
        language='en'
        output=gTTS(text=notice,lang=language,slow=False)

        output.save("output.mp3")

        os.system("start output.mp3")


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback
        time.sleep(5)
        

# Disconnect the device and application from the cloud
deviceCli.disconnect()
