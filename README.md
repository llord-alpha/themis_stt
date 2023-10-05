# themis_stt
Themis Text to Speech Module

## functions
log(message, startup):
        logs message to console (when `LOG_TO_CONSOLE` true) and log.txt
        log.txt clears on every startup


## classes

JsonParser(file_destination):
        when file_destinantion not found or file empty a new file: `gitignore/properties.json` is used or created

        JsonParser.get_json(key):
                returns value of `key` 

        JsonParser.write_json(key, value)
                writes key and value into json. if json file does not exist, a new one is created
        JsonParser.checkexistance(key=None)
                checks if Item `key` exists
                if key == None --> checks if json file exists



# properties.json:
`API_TOKEN`             :   Token to the **assemblyai**  API (currently not in use)

`SELECT_AUDIOINPUT`     :   Determines if user selects:
                            * audio input interactively:    {"SELECT_AUDIOINPUT" : true}
                            * uses default audio Device:    {"SELECT_AUDIOINPUT" : false}
                            * preselects Audioinput:        {"SELECT_AUDIOINPUT" : x}   , where x is the Input Device id of the desired audio device or the name of the device (e.g. "Microphone (Logi C270 HD WebCam)" ). 

`LOG_TO_CONSOLE`        :   * true:     outputs error messages and warnings to console
                            * false:    only logs error messages and warnings to the log

