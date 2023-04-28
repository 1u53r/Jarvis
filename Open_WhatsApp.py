
from listen import MicExecution
from speak import Speak
import pyautogui
import time


def Open_WhatsApp():
    Speak('opening, whatsapp')
    Speak("To whom should I send the message")
    Whom = MicExecution().lower()
    pyautogui.hotkey('win','r')
    pyautogui.hotkey('ctrl','x')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('https://web.whatsapp.com/')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(Whom)
    Speak("What should I send")
    send = MicExecution().lower()
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.write(send)# space it compulsury
    pyautogui.press('enter')
    Speak(f'Done, message {send} to {Whom}')
# Open_WhatsApp()