

import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from listen import MicExecution

def OpenExe(Query):
    Query =str(Query).lower()


    if "visit" in Query:
        NameOfWeb = Query.replace("visit ","")
        Link = f"https://www.{NameOfWeb}.com"
        webbrowser.open(Link)

    elif "open" in Query:
        NameOfTheApp = Query.replace("Open ","")
        try:
            if "chrome" in NameOfTheApp:
                os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

            elif "code" in Query:
                os.startfile(r"C:\Users\mtauh\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        except:
            print('starting exception handeling')
            pyautogui.press('win')
            sleep(1)
            keyboard.write(NameOfTheApp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
        return True

    elif "start" in Query:
        NameOfTheApp = Query.replace("Open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(NameOfTheApp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
