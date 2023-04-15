from Brain.Aibrain import ReplyBrain
from body.listen import MicExecution
print("Initializing Jarvis...")
from body.speak import Speak
from Brain.qna import QuestionReplier
import speech_recognition as sr
from main import MainTaskExecution
from Advance_features.open_youtube import Play_youtube
from Advance_features.Open_WhatsApp import Open_WhatsApp
from Advance_features.ShutDown import DeepSleep


def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # by 8 this is the time in which ai will start listing again

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""

    query = str(query).lower()
    print(query)
    return query


def MainExecution():
    Speak("Hello sir")
    Speak("available sir, always for you")
    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif "activate deep sleep" in Data or "intiallize deep sleep" in Data:
            DeepSleep()

        elif "on whatsapp" in Data:
            Open_WhatsApp()
        
        elif "on youtube" in Data:
            Speak("Which music would you like me to play")
            Play_youtube()

        elif len(Data)<3:
            pass
        
        elif "who is amanya" in Data or "who is baccha" in Data: # specific command.
            Speak("she is your love")

        elif "mean of jarvis" in Data or "mean of your name" in Data:
            Speak("My name is means, Just a really very intellegent system")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionReplier(Data)
            Speak(Reply)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def wake_up():
    query = Listen().lower()
    
    if "wake up" in query:
        print("")
        print("waking up")
        print("")
        MainExecution()
    else:
        pass

wake_up()