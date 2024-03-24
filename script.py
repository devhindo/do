import speech_recognition as sr
import pyperclip
import pyautogui

# create recognizer and mic instances
recognizer = sr.Recognizer()
microphone = sr.Microphone()

while True:
    # listen to the microphone
    with microphone as source:
        print("Say something!")
        audio = recognizer.listen(source)

    try:
        # recognize speech using Google Speech Recognition
        words = recognizer.recognize_google(audio)
        print(words)

        # perform command if 'paste' is heard
        if 'paste' in words:
            pyperclip.paste()
        elif 'stop listening' in words:
            break
        if 'paste' in words:
            clipboard_content = pyperclip.paste()
            pyautogui.write(clipboard_content)
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")