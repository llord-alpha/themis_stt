import vosk
import speech_recognition

rec = speech_recognition.Recognizer()


with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = rec.listen(source)

print(rec.recognize_vosk(audio))
# print(rec.recognize_whisper_api(audio))