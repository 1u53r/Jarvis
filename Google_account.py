from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
executable_path = '/home/machine/Downloads/programs/database/chromedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(executable_path=executable_path,options= chrome_options)
gmail_Signup = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
browser.get(gmail_Signup)
browser.maximize_window()
time.sleep(3)

Mob_Number = input('Enter Your Mobile Number : ')
IN_First_name = input("Enter Your first name : ")
Ls_First_name = input("Enter Your last name : ")

First_name = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input")
First_name.click()
First_name.send_keys(IN_First_name)
time.sleep(2)

Last_name = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input")
Last_name.click()
Last_name.send_keys(Ls_First_name)
time.sleep(2)

UserName = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
UserName.click()
UserName.send_keys("Randombfdbr5")
time.sleep(2)

Password = browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input")
Password.click()
Password.send_keys("%jhvsajkcaljbs86313")
time.sleep(2)

Confirm_Password = browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
Confirm_Password.click()
Confirm_Password.send_keys("%jhvsajkcaljbs86313")
time.sleep(2)

Next_1 = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
Next_1.click()
time.sleep(5)

Phone_Number = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div[2]/div[1]/label/input")
Phone_Number.click()
Phone_Number.send_keys(Mob_Number)
time.sleep(2)

Next_2 = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
Next_2.click()
time.sleep(20)

Verify = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
Verify.click()
time.sleep(5)

Clear_mob_Number = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div[1]/label/input")
Clear_mob_Number.clear()
time.sleep(1)

Recovery_Email = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
Recovery_Email.click()
Recovery_Email.send_keys("Randombfdbr5245@gmail.com")
time.sleep(2)

Day = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/input")
Day.click()
Day.send_keys("01")

Month = Select(browser.find_element(by=By.XPATH, value= '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[2]/div/div/div[2]/select'))
Month.select_by_visible_text('January')
time.sleep(2)

Year = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div/div[1]/div/div[1]/input")
Year.click()
Year.send_keys("2001")
time.sleep(2)

Gender = Select(browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[4]/div[1]/div/div[2]/select"))
Gender.select_by_visible_text('Female')
time.sleep(2)

Next_3 = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
Next_3.click()
time.sleep(5)

I_Agree = browser.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
I_Agree.click()
time.sleep(8)

Success = browser.find_element(By.XPATH,value="/html/body/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/h1")

if Success==True:
    print("!!!!!!!!Account created Successfully!!!!!!")

else:
    print("Error Occured!!!")