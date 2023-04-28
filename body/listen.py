

import speech_recognition as sr
from googletrans import Translator
# googletrans==3.1.0a0
# 1 translate fuction for voice hindi to english.

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # by 8 this is the time in which ai will start listining again

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")

    except:
        return ""

    query = str(query)
    return query.lower()

# 2 hindi to englise translator

def TranslationHinToEng(Text):
    line =str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you said : {data}")
    return data

# # # 3 - connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

# MicExecution()
# Listen()