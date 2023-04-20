########################### Installing reqiuired packages
from contextlib import contextmanager
import sys, os
import subprocess
imp = ['pyttsx3', 'selenium==4.1.3']
modules = []

for x in imp:
    try:
        modules.append(__import__(x))
        print(f"Found {x}.")
    except:
        @contextmanager
        def suppress_stdout():
            with open(os.devnull, "w") as devnull:
                old_stdout = sys.stdout
                sys.stdout = devnull
            try:  
                yield
            finally:
                sys.stdout = old_stdout
        print(f"{x} Not Found")
        print("Installling required packages.........")
        with suppress_stdout():
            for x in imp:
                def install(package):
                        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                install(x)
        print("Packages installed successfully")
        print("Intiating the script...")

    else:
        print(f"Facing error while installing {x}")




#### Windows based
import pyttsx3

# def Speak(Text):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty("voices")
#     engine.setProperty('voices', voices[0].id)
#     engine.setProperty('rate',170)
#     print("")
#     print(f"You : {Text}.")
#     print("")
#     engine.say(Text)
#     engine.runAndWait()
# Speak("Hello sir")


######  Chrome based 

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
Path = "chromedriver.exe"
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website =  r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value= '/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def speak(Text):

    lengthoftext = len(str(Text))

    if lengthoftext==0:
        pass
    else:
        print("")
        print(f" AI : {Text}")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()


        if lengthoftext>=30:
            sleep(4)
        elif lengthoftext>=40:
            sleep(6)
        elif lengthoftext>=55:
            sleep(8)
        elif lengthoftext>=70:
            sleep(10)
        elif lengthoftext>=100:
            sleep(13)

        elif lengthoftext>=120:
            sleep(14)

        else:
            sleep(2)
