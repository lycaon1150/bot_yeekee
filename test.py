from re import I
from selenium import webdriver
import selenium
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
# from seleniumrequests import Chrome
import datetime

import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument('window-size=1920x1080')

usr=str('punlerd1150') 
userlist = ['punlerd1150','knowdeep01','knowdeep02']
pwd=str('Punlerd1150') 

driverlist = []
key_click = []
input_number_list = []

for n,item in enumerate(userlist):

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    sleep(1)
    print("opened chome")
    driver.get('https://www.jetsada.net/member')
    print ("Opened jetsada")
    sleep(1)
    # driver.save_screenshot("path to save screen.jpeg")
    login_box = driver.find_element_by_class_name('btn-login-modal')
    login_box.click()

    username_box = driver.find_element_by_id('username')
    username_box.send_keys(str(item))
    print ("Id entered")
    sleep(1)
    
    password_box = driver.find_element_by_id('password')
    password_box.send_keys(pwd)
    print ("Password entered")
    
    login_box = driver.find_element_by_class_name('btn-100')
    login_box.click()

    sleep(2)
    driver.get("https://www.jetsada.net/member/lottery/yeekee/407")

    click_number = driver.find_element_by_class_name('shoot-number-tab')
    click_number.click()

    sleep(0.5)

    input_number = driver.find_element_by_class_name('input-key-num')
    input_number.send_keys(11111)

    driverlist.append(driver)

    random_number = driver.find_element_by_class_name('btn-shoot-plus')

    key_click.append(random_number)

    input_number_list.append(input_number)
    sleep(0.5)


# dataSend = {"number":"12345","bet_category_id":251,"yeekee_special":""}




start = 500000
while(1):
    now = datetime.datetime.now()
    if now.second % 20 == 19 and now.microsecond > start: #152500

        for n , driver in enumerate(driverlist):
            key_click[n].click()
            print(now.microsecond)
            


        # start = start + 0
        time.sleep(1)
        
        for n , driver in enumerate(driverlist):
            number = int(n*11111)
            input_number = driver.find_element_by_class_name('input-key-num')
            input_number.send_keys(number)

    
    

print('done')
    


# random_number = driver.find_element_by_class_name('btnYeekeeSubmit')
random_number = driver.find_element_by_class_name('btn-shoot-plus')
random_number.click()

# print(response.text)

print ("Done")
input('Press anything to quit')
# driver.quit()
# print("Finished")