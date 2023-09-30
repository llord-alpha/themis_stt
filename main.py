import websocket
import base64
import pyaudio
import json
from threading import Thread


YOUR_API_TOKEN = "f7c7bb1fa5194b93a9caadc4fe174370" 
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 16000
p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=48000,         #SAMPLE_RATE, unhsprunglich 'RATE'
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
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