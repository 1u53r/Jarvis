
#################################################### Installing reqiuired packages  ################################################
import sys, os
import subprocess
imp = ['nltk',"torch","numpy","random","json",'keyboard','webbrowser','dotenv','openai','speech_recognition', 'googletrans','pyaudio','pyautogui','bs4','googleapiclient','pyttsx3', 'selenium']
pack = ['nltk',"torch","numpy","random","json",'keyboard','python-dotenv','openai','SpeechRecognition','googletrans==3.1.0a0','PyAudio','PyAutoGUI','bs4','google-api-python-client','pyttsx3', 'selenium==4.1.3']
modules = []

for x in imp:
    try:
        modules.append(__import__(x))
        print(f"Found {x}.")
    except ImportError:
        print(f"{x} Not Found")
        print("Installling required packages.........")
        for x in pack:
            def install(package):
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            install(x)
        print("Packages installed successfully")
        print("Intiating the script...")

    except:
        print(f"Facing error while installing {x}")
