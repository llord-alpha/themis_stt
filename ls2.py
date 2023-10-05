import vosk
import speech_recognition

rec = speech_recognition.Recognizer()

mic = speech_recognition.Microphone()
print(type(mic.list_microphone_names()))
for i in mic.list_microphone_names():
    print("Audiodevice " , mic.list_microphone_names().index(i) , ":  - " , i)

testmic = speech_recognition.Microphone(device_index=999)

print(mic.list_microphone_names())

with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = rec.listen(source)

print(rec.recognize_sphinx(audio))




OPENAI_API_KEY = "INSERT OPENAI API KEY HERE"
try:
    print(f"Whisper API thinks you said {rec.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
except speech_recognition.RequestError as e:
    print("Could not request results from Whisper API")


# print(rec.recognize_whisper_api(audio))