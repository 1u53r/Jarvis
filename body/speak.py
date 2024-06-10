######  Chrome based 

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "database\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

website =  r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value= '/html/body/div[2]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')
driver.execute_script("window.scrollBy(0,500);")

def Speak(Text):
    lengthoftext = len(str(Text))   

    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f" AI : {Text}")
        Data = str(Text)
        xpathofsec = '/html/body/div[2]/div[2]/form/textarea'
        
        try:
            input_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpathofsec))
            )
            input_field.send_keys(Data)
            driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/form/input[1]').click()
            driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/form/textarea').clear()
        
            # Adjust sleep time according to the length of the text
            if lengthoftext >= 30:
                sleep(4)
            elif lengthoftext >= 40:
                sleep(6)
            elif lengthoftext >= 55:
                sleep(8)
            elif lengthoftext >= 70:
                sleep(10)
            elif lengthoftext >= 100:
                sleep(13)
            elif lengthoftext >= 120:
                sleep(14)
            else:
                sleep(6)
        except Exception as e:
            print("An error occurred:", e)


Speak("I was missing you so much, Finally you are back, let's start a new project")