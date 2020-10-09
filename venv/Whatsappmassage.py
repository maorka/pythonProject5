from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
def Whatappmassagefunction(allert):

 options = webdriver.ChromeOptions()
 options.add_argument("user-data-dir=C:/Users/מאור קרקוקלי/AppData\Local/Google/Chrome/User Data/Default")
 driver = webdriver.Chrome(executable_path=r'D:/PythonProjects/whatsappmaagse/newfolder/chromedriver', chrome_options=options)

 driver.get("https://web.whatsapp.com/")
 wait = WebDriverWait(driver, 600)

 # Replace 'Friend's Name' with the name of your friend
 # or the name of a group
 target = '"Test"'

 # Replace the below string with your own message
 #string = 'Parking was found!!!'

 x_arg = '//span[contains(@title,' + target + ')]'
 group_title = wait.until(EC.presence_of_element_located((
    	By.XPATH, x_arg)))
 group_title.click()
 inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
 input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))
 for i in range(1):
	 input_box.send_keys('w'+allert + Keys.ENTER)
	 time.sleep(1)

 return ()


