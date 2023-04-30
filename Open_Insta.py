# from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from listen import MicExecution
from speak import Speak

from Data import Username,Password
def Instagram():
    browser = webdriver.Chrome('database/chromedriver.exe',options=chrome_options)
    browser.get('https://www.instagram.com/')
    browser.maximize_window()
    time.sleep(4)


    #input

    UserName = browser.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
    UserName.send_keys(Username)
    time.sleep(1)

    PassWord = browser.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
    PassWord.send_keys(Password)
    PassWord.submit()
    time.sleep(5)
    # driver.implicitly_wait(20)    #Notnow
    login = browser.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
    login.click()
    time.sleep(5)

    #Notification
    browser.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(3)

    Message = browser.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/a/div/div[2]/div/div')
    Message.click()
    time.sleep(2)

    Send_message = browser.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[3]/div")
    Send_message.click()
    time.sleep(1)

    Type_message= browser.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")
    Type_message.click()
    Speak("sir, what should I send him?")
    message = MicExecution().lower()
    Type_message.send_keys(message)

    Type_message_send = browser.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")
    Type_message_send.click()
    Speak("message done sir")
Instagram()
