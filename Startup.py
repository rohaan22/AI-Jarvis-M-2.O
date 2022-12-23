from PyQt5.QtWidgets import *
from MainCode import Speak
import speech_recognition as sr
import sys


WakeWord1 = "hey jarvis"
WakeWord2 = "wake up"
WakeWord3 = "get up"


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
    try:
        print(": Recognizing.....")
        query = r.recognize_google(audio, language='en-pk')
    except:
        return ""
    query = str(query).lower()
    return query


def Pass(pass_inp):
    password = "python"
    passss  = str(password)
    if passss==str(pass_inp):
        Speak("Access Granted .")
        Speak("For more verification I will verify your face...")
        Speak("Please look in to the camera...")
        from DataBase.FaceDetectionModule.FaceRecognition import FaceRocog
        FaceRocog()
              
    else:
        Speak("Access Not Granted .")
        sys.exit()


def Wake():
    while(True):
        q = Listen()
        if WakeWord1 in q or WakeWord2 in q or WakeWord3 in q:
            Speak("Jarvis program is password protected...")
            Speak("Kindly provide the correct password to access.")
            passs = input("Enter the correct password: ")
            Pass(passs)

        elif "terminate" in q:
            Speak("Ok sir terminating")
            sys.exit()


if __name__=="__main__":
    Wake()