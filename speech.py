import speech_recognition as sr
import pyttsx3

def speech():
    try:
        a = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google speech recognition could not understand audio")
    except sr.RequestError:
        print("could not request results from the google speech recognition")

speech()