import websocket
import base64
import pyaudio
import json
import json
import time 

########## SETTINGS ##########

SELECT_AUDIOINPUT = False   # True = select audio input device, False = use default input device
















########## /SETTINGS ##########

# load API_TOKEN from statics.json
statics = open('gitignore/properties.json')
data = json.load(statics)
YOUR_API_TOKEN = data["API_TOKEN"]
statics.close()


def select_audioinput():
    """
    returns the index of the audio input device
    """
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
    
    device_id = int(input("Select input device id: "))
    return device_id

if SELECT_AUDIOINPUT:
    input_device = select_audioinput()
else:
    input_device = None


# stream settings
FRAMES_PER_BUFFER = 3200                        
FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 16000

# intialize stream
p = pyaudio.PyAudio()

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