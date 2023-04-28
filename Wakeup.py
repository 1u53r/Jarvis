import speech_recognition as sr 
from body.speak import speak
from body.listen import Listen

def WakeupDetected():

    queery = Listen().lower()

    if "wake up jarvis" in queery:
        speak("available sir, always for you")
        
        queery = Listen().lower()

        if "hello" in queery:
                speak("Hi! i am jarvis!")

        elif "bye" in queery:
            speak("Bye sir!")

        else:
            pass
    else:
        pass

# WakeupDetected()