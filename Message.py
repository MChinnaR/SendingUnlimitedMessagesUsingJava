from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#https://chromedriver.chromium.org/downloads
#Downlode the crome driver as per the ur chrome version
#After that give the path


browser = webdriver.Chrome("K:\Downlodes\chromedriver_win32\chromedriver.exe")
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 600)

#Scan with whatsapp web

target = '"enter contact name here"' #enter contact name here
string = "Message" #target msg
x_arg = ' //span[contains(@title, ' + target +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
# _2A8P4 This class name may be different see the photo in folder to change
input_box = browser.find_element_by_class_name('_2A8P4')
for i in range(1):
    input_box.send_keys(string + Keys.ENTER)
    #time.sleep(1) # This line is used to delay the message time
