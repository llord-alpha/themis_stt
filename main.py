
import json
import os
import os.path
import time 
import speech_recognition



#
#       properties.json destination
#
properties_destination = "gitignore/properties.json"
#
#
#

#API_TOKEN_OAI = os.getenv("OAI_api_key")
#print(API_TOKEN_OAI)



# logging

def log(message, startup=None ):
    global LOG_TO_CONSOLE

    if startup:
        with open('log.txt', 'w') as f:         # clear old log
            f.write("--------------------------------------------------\n")
            f.write("This is the Log of the Themis Voice to Text Module\n")
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
                

class JsonParser:
    def __init__(self, destination = None):

        # set defult destination for json file
        defult_destination = "gitignore/properties.json" 


        if destination == None:                     # if no destination is specified, use standart destination
            log(str("No destination specified. Use standart destination: " + defult_destination))
            destination = defult_destination
        self.destination = destination
        try:
            log("Loading JSON File:")
            with open(self.destination, "r") as f:      # load json contentsn
                self.data = json.load(f)
        except:
            with open(self.destination, "w") as f:    # create new json file if file is empty   
                log(str("JSON File -->" + destination + "<-- empty. Creating new file."))
                self.data = {}
                json.dump(self.data, f, indent=4)
    def checkexistance(self, key = None):
        if key == None:                                 # check if file exists
            return os.path.isfile(self.destination)
        else:
            try:                                        # check if entry exists
                self.data[key]
                return True
            except:
                return False
    def get_json(self, key):
        try:                                    # try to get value from json file
            with open(self.destination, "r") as f:
                self.data = json.load(f)
            return self.data[key]
        except:
            return None
    def write_json(self, key, value):           # write value to json file
        self.data[key] = value
        with open(self.destination, 'w') as f:
            json.dump(self.data, f, indent=4)

# user selects audio input device

def usr_select_audioinput():
    device_id = -1                                      # initialize device_id with -1 to enter while loop
    logmsg_long = ""                                    # initialize logmsg_long with empty string for cleaner text Output
    working_mics = ""
    usr_selected_id = ""
    while True :
        logmsg_long = ""  
        logmsg_long = logmsg_long +"Available input devices: \n"
        working_mics = speech_recognition.Microphone.list_working_microphones()
        time.sleep(0.5)
        for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
            if index in working_mics:
                msg = "Microphone with name \"{1}\"  ----> `Microphone (device_index={0})`".format(index, name) + "\n"
                logmsg_long = logmsg_long + msg
        log(logmsg_long)


        usr_selected_id = input("Select input device id: ")

        try:
            device_id = int(usr_selected_id)
        except:
            log("Please enter a valid device id")
            continue
        time.sleep(0.5)
        try:
            if device_id in working_mics:
                speech_recognition.Microphone(device_index = device_id)
                log("Device found" + "\n" + "Device id: " + str(device_id) + "\n" + "Device name: " + speech_recognition.Microphone.list_microphone_names()[device_id])
                break
        except:
            pass

        print("Device not found, please try again. ")
        device_id = -1                                  # resets device_id to -1 to enter while loop again
        logmsg_long = ""                            # clears logline for next loop

    return device_id


# startup
log("Starting up", startup=True)
LOG_TO_CONSOLE = True

# load from properties.json
jsn_parser = JsonParser(properties_destination)

API_TOKEN_AAI = jsn_parser.get_json("API_TOKEN_AAI")   # API Token from AssemblyAI
USER_SELECT_AUDIOINPUT = jsn_parser.get_json("SELECT_AUDIOINPUT")   # True = select audio input device, False = use default input device
LOG_TO_CONSOLE = jsn_parser.get_json("LOG_TO_CONSOLE")     # True = log errors to console, False = do not log errors to console





# select mode for audio input selection
log("Selecting audio input device ......")
MICROPHONE_index = None
if USER_SELECT_AUDIOINPUT == True and type(USER_SELECT_AUDIOINPUT) == bool:
    log("User selects input device")
    MICROPHONE_index = usr_select_audioinput()
elif not USER_SELECT_AUDIOINPUT:
    log("Using system default input device")
    MICROPHONE_index = None
elif type(USER_SELECT_AUDIOINPUT) == str:
    try:
        if USER_SELECT_AUDIOINPUT in speech_recognition.Microphone.list_microphone_names():
            MICROPHONE_index = speech_recognition.Microphone.list_microphone_names().index(USER_SELECT_AUDIOINPUT)
            log("Device found" + "\n" + "Device id: " + str(MICROPHONE_index) + "\n" + "Device name: " + speech_recognition.Microphone.list_microphone_names()[MICROPHONE_index])
    except:
        log("CRITICAL: User defined input device not found, using system default input device instead")
        MICROPHONE_index = None
else:
    try:
        speech_recognition.Microphone(device_index = USER_SELECT_AUDIOINPUT)
        log("Device found" + "\n" + "Device id: " + str(USER_SELECT_AUDIOINPUT) + "\n" + "Device name: " + speech_recognition.Microphone.list_microphone_names()[USER_SELECT_AUDIOINPUT])       
    except:
        log("CRITICAL: User defined input device not found, using system default input device instead")
        MICROPHONE_index = None



rec = speech_recognition.Recognizer()
with speech_recognition.Microphone(device_index = MICROPHONE_index) as source:
    log("Say something!")
    audio = rec.listen(source)

log(rec.recognize_whisper_api(audio, api_key = API_TOKEN_OAI))
