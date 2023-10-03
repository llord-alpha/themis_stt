import vosk
import speech_recognition

rec = speech_recognition.Recognizer()
top = vosk.Model("model")
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = rec.listen(source)

print(rec.recognize_vosk(audio, model=top))