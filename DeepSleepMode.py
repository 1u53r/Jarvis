import pyautogui
from speak import Speak 
# from Advance_features.speak import Speak

def DeepSleep_mode():
    Speak('intiallizing System sleep mode')
    pyautogui.hotkey('win','d')
    pyautogui.hotkey('alt','f4')
    pyautogui.press('enter')

