import speech_recognition as sr
import pyperclip

# create recognizer and mic instances
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# listen to the microphone
with microphone as source:
    print("Say something!")
    audio = recognizer.listen(source)

# recognize speech using Google Speech Recognition
words = recognizer.recognize_google(audio)

# perform command if 'paste' is heard
if 'paste' in words:
    pyperclip.paste()
