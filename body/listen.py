import subprocess
import speech_recognition as sr
from googletrans import Translator
#it shouold be same as pip install googletrans==4.0.0-rc1


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)  # by 8 this is the time in which AI will start listening again

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

    query = str(query)
    return query.lower()

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line,dest='en')
    data = result.text
    print(f"Translated text: {data}")
    return data

def MicExecution():
    query = Listen()
    if query:
        data = TranslationHinToEng(query)
        return data
    else:
        return "No input received."