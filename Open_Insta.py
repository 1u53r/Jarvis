from bs4 import BeautifulSoup
from selenium import webdriver
import time

import soupsieve
from Data import Username, Password
browser = webdriver.Chrome('database\\chromedriver.exe')
browser.get('https://www.instagram.com/')
browser.maximize_window()
time.sleep(4)


#input

UserName = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
UserName.send_keys(Username)
time.sleep(1)

PassWord = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
PassWord.send_keys(Password)
PassWord.submit()
time.sleep(5)

#Notnow

NotNow = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
NotNow.click()
time.sleep(3)

#Notification

Noti = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
Noti.click()
time.sleep(5)

Massage = browser.find_element_by_xpath('//*[@id="mount_0_0_Rc"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[1]/div/div[3]/div/div[2]/a/svg').click()
time.sleep(3)

# soup = BeautifulSoup(browser.page_source, features='html.parser')
# new_message = soup.find_all("div", {"class":"41V_T   Sapc9                 Igw0E     IwRSH      eGOV         _4EzTm"}) 
# counter = 0 
# for i in new_message: 
#       counter += 1 
# print('Unread messages: ', counter)