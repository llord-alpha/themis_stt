import websocket
import base64
import pyaudio
import json
import time 




# logging

def log(message, startup=None ):
    global LOG_TO_CONSOLE

    if startup:
        with open('log.txt', 'w') as f:         # clear old log
            f.write("--------------------------------------------------\n")
            f.write("This is the Log of the Themis Voice to Text API\n")
            f.write("Startup time: " + time.strftime("%Y-%m-%d %Hh:%Ms:%Ss", time.localtime()) + "\n")
            f.write("Message: " + message + "\n")
            
    else:
        with open('log.txt', 'a') as f:         # append to log
            f.write("--------------------------------------------------\n")
            f.write("Time: " + time.strftime("%Y-%m-%d %Hh:%Ms:%Ss", time.localtime()) + "\n")
            f.write("Message: " + str(message) + "\n")
            
            if LOG_TO_CONSOLE:
                print("--------------------------------------------------")
                print("Time: " + time.strftime("%Y-%m-%d %Hh:%Ms:%Ss", time.localtime()))
                print("Message: \n" + message)
                


# user selects audio input device

def select_audioinput():
    """
    returns the index of the audio input device
    """
    device_id = -1
    logmsg_long = ""

    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    print("numdevices: ", numdevices)
    while device_id > numdevices or device_id < 0:
        
        logmsg_long = logmsg_long +"Available input devices: \n"
        for i in range(0, numdevices):
            print("i: ", i)
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                logmsg = "Input Device id " + str(i) + " - " + str(p.get_device_info_by_host_api_device_index(0, i).get('name'))
            logmsg_long = logmsg_long + logmsg + "\n"

        log(logmsg_long)
        device_id = int(input("Select input device id: "))
        if device_id > numdevices or device_id < 0:
           
            logmsg = "Device id out of range, please try again. device_id: " + str(device_id)
            log(logmsg)

    return device_id


# startup
log("Starting up", startup=True)


# load from properties.json
properties = open('gitignore/properties.json')
data = json.load(properties)

YOUR_API_TOKEN = data["API_TOKEN"]
USER_SELECT_AUDIOINPUT = data["SELECT_AUDIOINPUT"]   # True = select audio input device, False = use default input device
LOG_TO_CONSOLE = data["LOG_TO_CONSOLE"]     # True = log errors to console, False = do not log errors to console


properties.close()



# stream settings
FRAMES_PER_BUFFER = 3200                        
FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 16000

# intialize stream
p = pyaudio.PyAudio()







# select mode for audio input selection
if USER_SELECT_AUDIOINPUT == True:
    input_device = select_audioinput()
elif not USER_SELECT_AUDIOINPUT:
    input_device = None
else:
    try:
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        print("numdevices: ", numdevices)
        if int(USER_SELECT_AUDIOINPUT) <= numdevices:
            input_device = int(USER_SELECT_AUDIOINPUT)
        elif int(USER_SELECT_AUDIOINPUT) > numdevices:
#            print("Device id out of range, using system default input device instead")
            log("Device id out of range, using system default input device instead")
            input_device = None
    except:
#        print("Cannot find input device, using system default input device instead")
        log("User defined input device not found, using system default input device instead")
        input_device = None




stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = 48000,         #SAMPLE_RATE, uhsprunglich 'RATE'
    input = True,
    frames_per_buffer = FRAMES_PER_BUFFER,
    input_device_index = input_device   
)

def on_message(ws, message):
    """
    is being called on every message
    """
    pass


def on_open(ws):
    """
    is being called on session start
    """
    pass


def on_error(ws, error):
    """
    is being called in case of errors
    """
    pass


def on_close(ws):
    """
    is being called on session end
    """
    pass


# Set up the WebSocket connection with your desired callback functions
websocket.enableTrace(False)

# After opening the WebSocket connection, send an authentication header with your API key
auth_header = {"Authorization": YOUR_API_TOKEN }

ws = websocket.WebSocketApp(
    f"wss://api.assemblyai.com/v2/realtime/ws?sample_rate={SAMPLE_RATE}",
    header=auth_header,
    on_message=on_message,
    on_open=on_open,
    on_error=on_error,
    on_close=on_close
)


# Start the WebSocket connection
ws.run_forever()