# themis_stt
Themis Text to Speech Module

# functions
log(message, startup):
        logs message to console (when `LOG_TO_CONSOLE` true) and log.txt
        log.txt clears on every startup
        
# properties.json:
`API_TOKEN`             :   Token to the **assemblyai**  API

`SELECT_AUDIOINPUT`     :   Determines if user selects:
                            * audio input interactively:    {"SELECT_AUDIOINPUT" : true}
                            * uses default audio Device:    {"SELECT_AUDIOINPUT" : false}
                            * preselects Audioinput:        {"SELECT_AUDIOINPUT" : x}   , where x is the Input Device id of the desired audio device

`LOG_TO_CONSOLE`        :   * true:     outputs error messages and warnings to console
                            * false:    only logs error messages and warnings to the log

