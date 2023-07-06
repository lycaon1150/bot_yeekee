import code
# from curses import reset_shell_mode
import datetime
# from ensurepip import version
from lib2to3.pgen2 import driver
# from logging import exception
# import multiprocessing
import pickle
import random
import re
# import sched
import subprocess
import sys
import time
from typing import Tuple
from webbrowser import get
import requests
import json

# from multiprocessing import Process , Queue
# from re import I
# from threading import Thread
from time import sleep

import selenium
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By

import js_code

import paramiter as setting
import os




file_part = os.path.dirname(os.path.realpath(__file__))
version_yeekee = "v1.29"
print(datetime.datetime.now())

print(version_yeekee)
# external_ip = requests.get('https://api.ipify.org').text
# print(external_ip)

external_ip = "You know who am I"


class yeekee_bot(object):
    def __init__(self, json_user):
        self.json_user = json_user
        self.session_data = {}
        self.room_url = ""
        self.room_number = ""
        self.state = ""
        self.use_time = 0
        self.number_send = ""
        self.driver = ''
        self.bonus = 0
        self.display = Display(visible=0, size=(800, 800)) 
        self.movewinbet_url = ""
        self.mungmeelt_uid = ""
        
        print('success created')
        
    def get_bonus_vip(self,user,host):
        
        try:
            state = 0
            code = self.session_data[user]['authorization']
            if host == "nakee" :
                
                
                print('check VIP level')
                data_vip = self.driver.execute_script(js_code.check_vip_nakee(code))

                
                
                for j in range(90):
                    a = data_vip['data']['data'][j]['status']
                    
                    if a == "null":
                        state = 0;
                    elif a == "bonus":
                        
                        state = j+1;
                        break;
                    
                    
                if (state == 0):
                    print('no vip get')
                    
                else:
                    print("Get Bonus  " + str(state))
                    data_vip = self.driver.execute_script(js_code.get_vip_nakee(code,state))
                    
                    
            elif host == "ltobet":
                print('check VIP level')
                data_vip = self.driver.execute_script(js_code.check_vip_ltobet(code))

                
                
                for j in range(90):
                    a = data_vip['data']['data'][j]['status']
                    
                    if a == "null":
                        state = 0;
                    elif a == "bonus":
                        
                        state = j+1;
                        break;
                    
                    
                if (state == 0):
                    print('no vip get')
                    
                else:
                    print("Get Bonus  " + str(state))
                    data_vip = self.driver.execute_script(js_code.get_vip_ltobet(code,state))
                
            
            elif host == "thailotto":
                
                self.driver.execute_script(js_code.post_bonus_thailotto())
                
            
            
            else:
                print('Only Cj can get VIP process')
        except:
            print("get_bonus_vip error")
            

    def launchBrowser(self,server,host):
        
        
        options = uc.ChromeOptions()
        
        # options.add_argument('window-size=1920x1080')
        # options.add_argument('whitelisted-ips')
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        # options.add_argument("enable-automation")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-web-security")
        # options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-gpu")
        options.add_argument("--incognito")
        
        if server == "aws":
            if host == 'nakee':
                self.display.start()
            else:
                options.add_argument("--headless")
                
            self.driver = uc.Chrome(version_main=93, options=options)  
        elif server == "digitalocean":
            self.driver = uc.Chrome(version_main=100, options=options)  

        

    def create_connection(self):
        
        PROXY = "Selnyolycaon:F7k1KtH@154.16.11.95:45785"
        
        

        print('start create_connection')

        for user in self.json_user.keys():
            
            
 
            

            data_id = self.json_user[user]

            self.launchBrowser(data_id['sever'],data_id['host'])
              
            
            
            

            json_data = data_id
            
            self.driver.get('https://api.ipify.org')
            sleep(1)
            self.driver.save_screenshot('pic_ip.png')
            # json_data['driver'] = driver
            json_data['authorization']  = ''
            self.driver.delete_all_cookies()
            
            try:
                
                sleep(2)
                json_data['authorization'] = self.login( json_data['host'],json_data['ID'], json_data['Password'], json_data['url'])
                sleep(2)
                
                
            except:
                print('error with login')
                return 0
        
            
            self.session_data[user] = json_data
            
            
            if json_data['authorization']  == '':
                return 0
            else:
                return 1 
            

    def login(self, host, id, pwd, url):
        r = ''
        print(url)
        self.driver.get(url)
        sleep(5)
        self.driver.save_screenshot('pic_home.png')
        print(self.driver.execute_script('return navigator.webdriver'))
        
        
        if host in [ 'jetsada' , 'huay' , 'thailotto' , 'ruay' , 'lottovip' ]:
            
            if host == 'jetsada':
                self.driver.execute_script("document.getElementsByClassName('btn btn-bar btn-border btn-login-modal')[0].click();")
                class_username = 'username'
                sleep(1)
            elif host == 'thailotto':
                self.driver.execute_script("document.getElementsByClassName('btn btn-bar btn-login-modal')[0].click();")
                sleep(1)
                
            
            self.driver.execute_script("document.getElementsByName('username')[0].value='%s';" % str(id))
            self.driver.execute_script("document.getElementsByName('password')[0].value='%s';" % str(pwd))
            sleep(1)
            
            if host in [ 'jetsada' , 'huay' , 'thailotto' ] :
            
                self.driver.execute_script("document.querySelectorAll('button[type=submit]')[1].click();")
                sleep(2)
                r = self.driver.execute_script("return (await window.cookieStore.get('XSRF-TOKEN')).value")
            
            elif host in  ['ruay','lottovip'] :
                
                self.driver.execute_script("document.querySelectorAll('button[type=submit]')[0].click();")
                sleep(2)
                # self.driver.save_screenshot('pic_login.png')
                r = self.driver.execute_script("""a = document.cookie.split(';');c = '' ; for (let i = 0; i < a.length; i++) { b = a[i].split('=');if(b[0] == ' csrf_cookie'){c = b[1] }} return c; """)
                print(r)
            print('done login')
        
        
        elif host == 'lotto88':
            sleep(1)
            self.driver.find_element_by_xpath('//input[@type="text"]').send_keys(str(id))
            self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(str(pwd))
            sleep(1)
             
             
            self.driver.execute_script("document.getElementsByClassName('v-btn__content')[1].click()")
        
            sleep(5)
            r = self.driver.execute_script("return window.localStorage['ACCESS_TOKEN']")

        

        elif host == 'mungmeelt':
            
            sleep(1)
            self.driver.find_element(By.ID ,"username-login").send_keys(str(id))
            self.driver.find_element(By.ID ,"pw-login").send_keys(str(pwd))
            sleep(1)
             
            
            self.driver.execute_script("document.getElementsByClassName('mdc-button__label')[0].click()")
        
            sleep(2)
            
            # r = self.driver.execute_script("return window.localStorage['ACCESS_TOKEN']")
            self.mungmeelt_uid = self.driver.execute_script("return JSON.parse(window.localStorage[Object.keys(window.localStorage)[0]]).UserAttributes.at(3).Value")
            r = self.driver.execute_script("return window.localStorage[Object.keys(window.localStorage)[1]]")

            

        elif host == 'ltobet':
            
            sleep(2)
            # self.driver.execute_script("document.getElementsByClassName('form-control rounded-4 form-control-lg')[0].value = '%s';" % str(id))
            # self.driver.execute_script("document.getElementsByClassName('form-control rounded-4 form-control-lg')[1].value = '%s';" % str(pwd))
            sleep(1)
            self.driver.find_element_by_xpath('//input[@type="text"]').send_keys(str(id))
            self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(str(pwd))
            
            sleep(1)
            self.driver.execute_script("document.getElementsByClassName('btn btn-lg btn-primary w-100 mb-4 rounded-4 text-bold text-lg')[0].click()")
            
            sleep(5)
            r = self.driver.execute_script("return window.localStorage['auth._token.local']")
            
            
            
        
        elif host == 'nakee':
            
            for i in range(3):
                try:
                    sleep(2)
                    r = ""
                
                    print('try time login',i)
                    
                    print(self.driver.execute_script("return document.querySelectorAll('button[type=submit]')[0].disabled = false;"))
                    sleep(1)
                    self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys(str(id))
                    self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(str(pwd))
                    
                    sleep(3)
                    self.driver.execute_script("document.querySelectorAll('button[type=submit]')[0].click();")
                    sleep(4)
                    r = self.driver.execute_script("return window.localStorage['auth._token.local']")
                    
                    print('key == ',len(str(r)))
                    # key = self.driver.execute_script(js_code.login_nakee(id,pwd))
                    # print(key)
                    # r = str('Bearer ') + str(key['data']['token'])
                    
                    print('done login')
                    if len(str(r)) < 18:
                        self.driver.save_screenshot('pic_error_login.png')
                        self.driver.delete_all_cookies()
                        sleep(1)
                        self.driver.get(url)
                        sleep(3)
                        self.driver.save_screenshot('pic_home.png')
                    else:
                        break
                  
                
                except Exception as e:
                    print('error api login')
                    self.driver.quit()
                    self.launchBrowser(host)
                    sleep(3)
                    self.driver.delete_all_cookies()
                    self.driver.get(url)
                    
                    sleep(3)
                    
                    print('retry login')
                    print(e)
                    
        elif host == 'movewinbet':
                sleep(2)
                get_url = self.driver.current_url
                domain_1 = get_url.replace("https://", "")
                domian_name = domain_1.replace("/login", "")
                self.movewinbet_url = str(domian_name)
                
                self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(str(id))
                self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(str(pwd))
                sleep(1)
                
                
                self.driver.execute_script("document.querySelectorAll('button[type=submit]')[0].click();")
                
                
                
        sleep(3)
        self.driver.save_screenshot('pic_login.png')
        return r
        
    def room_88(self):
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        if time_in_minute < 240:
            state = int((time_in_minute-347+1440)/15)
            
        else:
            state = int((time_in_minute-347)/15)
        
        return state

    def room_264(self):
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        if time_in_minute < 240:
            state = int((time_in_minute-356+1440)/5)
            
        else:
            state = int((time_in_minute-356)/5)
        
        return state
    
    def room_264_movewinbet(self):
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        state = int((time_in_minute)/5)
    
        
        return state

    def get_result(self,user,bet_type):
        print('do process get_result')
        print('get rank')
        print(self.room_url)
        print(self.room_number)
        # _url = str('https://www.jetsada.net/member/lottery/yeekee/%s' %(start_number+state))

        self.driver.get(self.room_url)
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        sleep(3)
        self.driver.save_screenshot('rank.png')
        # print(self.room_url)
        
        name = user.split("_")[1]
        print(name)
        secret_name = ""
        
        if this_host == 'jetsada' or this_host == 'thailotto':
            n = 0
            
            self.driver.get(self.room_url)
            for c in name:
                if n == 3 or n == 4 or n == 5:
                    secret_name = str(secret_name) + str('*')
                else:
                    secret_name = str(secret_name) + str(c) 
                n = n + 1
            print(secret_name)
        
        
            for i in range(50):
                js = "return document.getElementsByClassName('username')[%s].innerText" %i
                find_name = self.driver.execute_script(js)
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1
            
            sleep(1)
            new_url = self.room_url + '?page=2'    
            self.driver.get(new_url)
        
        
            for i in range(50):
                js = "return document.getElementsByClassName('username')[%s].innerText" %i
                find_name = self.driver.execute_script(js)
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+51
        
        
        if this_host == 'movewinbet':
            n = 0
            
            self.driver.get(self.room_url)
            for c in name:
                if n == 1 or n == 2:
                    secret_name = str(secret_name) + str('*')
                else:
                    secret_name = str(secret_name) + str(c) 
                n = n + 1
            print(secret_name)

            try:
                self.bonus = 0
                js = "return document.getElementsByClassName('username').length"
                length_bonus = int(self.driver.execute_script(js))
                
                for i in range(length_bonus):
                    js = "return document.getElementsByClassName('username')[%s]" % str(i+1)
                    find_name = self.driver.execute_script(js).split('\n')[1]
                    if find_name == name or find_name == secret_name:
                        if bet_type == 'special':
                        
                            self.bonus = self.bonus + 300
                        else:
                            self.bonus = self.bonus + 500
                    
            except:

                pass
            
            
            for i in range(20):
                js = "return document.getElementsByClassName('item-col col-4 col-xl-4')[%s].innerText" % str(i*3+1)
                find_name = self.driver.execute_script(js).split('\n')[1]
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1
            
            sleep(2)
            new_url = self.room_url + '?page=2'    
            self.driver.get(new_url)
        
        
            for i in range(20):
                js = "return document.getElementsByClassName('item-col col-4 col-xl-4')[%s].innerText" % str(i*3+1)
                find_name = self.driver.execute_script(js).split('\n')[1]
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1+20
            
            
            sleep(2)
            new_url = self.room_url + '?page=3'    
            self.driver.get(new_url)
        
        
            for i in range(20):
                js = "return document.getElementsByClassName('item-col col-4 col-xl-4')[%s].innerText" % str(i*3+1)
                find_name = self.driver.execute_script(js).split('\n')[1]
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1+40
            
            sleep(2)
            new_url = self.room_url + '?page=4'    
            self.driver.get(new_url)
        
        
            for i in range(20):
                js = "return document.getElementsByClassName('item-col col-4 col-xl-4')[%s].innerText" % str(i*3+1)
                find_name = self.driver.execute_script(js).split('\n')[1]
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1+60 
            
        elif this_host == 'ltobet':
            z = len(name)
            n = 0
            
            secret_name = "xxxxxxx"
            secret_name = list(secret_name)
            for c in name:
                if n == 0:
                    secret_name[0] = str(c)
                    
                elif n == 1:
                    secret_name[1] = str(c)
                    
                elif n == z-1:  
                    secret_name[6] = str(c)
                    
                elif n == z-2:
                    secret_name[5] = str(c) 
                
                n = n + 1
                
                
            secret_name = str(''.join(secret_name))    
            print(secret_name)
            room = self.room_number
            number_send = self.number_send
            result = []
            number = []
            
            if bet_type == 'zodiac':
                max_room = 2
                reward_list = list(self.driver.execute_script(str(js_code.get_rank_ltobet(code,room,1,bet_type)))['userRewards'])
           
                for json_item in reward_list:
                    print(json_item)
                    if str(secret_name) == str(json_item['username']) and str(number_send) == str(json_item['number']):
                        self.bonus = json_item['reward']
                        
            else:
                max_room = 4
            
            print('bonus : ' + str(self.bonus))
            
            for i in range(1,max_room):
                _r = list(self.driver.execute_script(str(js_code.get_rank_ltobet(code,room,i,bet_type)))['records'])
                # print(_r)
                # random.randint(1, 3)
                for data in _r:
                    number.append(data['number'])
                    result.append(data['username'])

            
           
            for rank , username in enumerate(result):
              
                if str(secret_name) == str(username) and str(number_send) == str(number[rank]):
                    return rank+1
            
            
                
        elif this_host == 'nakee':
            z = len(name)
            n = 0
            
            secret_name = "xxxxxxx"
            secret_name = list(secret_name)
            for c in name:
                if n == 0:
                    secret_name[0] = str(c)
                    
                elif n == 1:
                    secret_name[1] = str(c)
                    
                elif n == z-1:  
                    secret_name[6] = str(c)
                    
                elif n == z-2:
                    secret_name[5] = str(c) 
                
                n = n + 1
                
                
            secret_name = str(''.join(secret_name))    
            print(secret_name)
            room = self.room_number
            number_send = self.number_send
            result = []
            number = []
            
            bonus_result =[]
            bonus_number =[]
            bonus_reward = []
            
            
            _bonus_data = list(self.driver.execute_script(str(js_code.get_bonus_nakee(code,room)))['userRewards'])
            
            print(_bonus_data)
            
            for data in _bonus_data:
                bonus_result.append(data['username'])
                bonus_number.append(data['number'])
                bonus_reward.append(data['reward'])
            
            for i , username in enumerate(bonus_result):
                if str(secret_name) == str(username) and str(number_send) == str(bonus_number[i]):
                    self.bonus = bonus_reward[i]
                    break
            
            
            for i in range(1,7):
                _r = list(self.driver.execute_script(str(js_code.get_rank_nakee(code,room,i)))['records'])
                # print(_r)
                sleep(0.3)
                for data in _r:
                    number.append(data['number'])
                    result.append(data['username'])

           
            for rank , username in enumerate(result):
              
                if str(secret_name) == str(username) and str(number_send) == str(number[rank]):
                    return rank+1
        
        elif this_host in  ['ruay','lottovip'] :
            print('wait 120 sec for get Rank')
            sleep(120)
            for i in range(1,4):
                _url_ruay = self.room_url + "/" + str(i)
                self.driver.get(_url_ruay)
                sleep(2)
                for j in range(20):
                    if str(self.number_send) == str(self.driver.execute_script("return document.getElementsByClassName('mb-0')[%s].textContent" % str(j))):
                        return (i-1)*20 + j+1
            
            
            
        print('end process get_result')
        return 0
        
    def get_room(self,user):
        print('get_room')
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        bet_type = self.session_data[user]['bet_type']
        
        start_number = 0
        state = 0 
        
        if this_host == 'jetsada':
            state = self.room_88()
            if bet_type == 'special':
                start_number = 354  # strat the number of url
            elif bet_type == 'normal':
                start_number = 172

            room = start_number+state 
            
        elif this_host == 'huay':
            if bet_type == 'normal':
                state = self.room_88()
                start_number = 161
            elif bet_type == 'special':
                state = self.room_264()
                start_number = 514
        
        elif this_host == 'thailotto':
            if bet_type == 'special':
                start_number = 450  
                state = self.room_264()
                
            elif bet_type == 'normal':
                start_number = 172
                state = self.room_88()
            
            room = start_number+state
            
        elif this_host == 'nakee':
            
            data_room_nakee = ""
            attempts = 0
            while attempts < 3:
                try:
                    print('get_room_by_js : ',attempts)
                    sleep(3)
                    data_room_nakee = self.driver.execute_script(js_code.get_room_nakee(code))
                
                    break
                except:
                    attempts = attempts + 1
               
            # print(data_room_nakee)

            if bet_type == 'special':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 1401:
                        start_number = int(item['id'])
                        break
                state = self.room_264()

            elif bet_type == 'vip_264':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 1701:
                        start_number = int(item['id'])
                        break
                state = self.room_264()
                
            elif bet_type == 'normal':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 101:
                        start_number = int(item['id'])
                        break
                
                state = self.room_88()
            
            elif bet_type == 'vip_88':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 201:
                        start_number = int(item['id'])
                        break
                    
                state = self.room_88()
                
            room = start_number+state 
            
        elif this_host == 'ltobet':
            
            data_room_nakee = ""
            attempts = 0
      
            if bet_type == 'special':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('speed',code))
                state = self.room_264()
                room = data_room_nakee['records'][state]['id']
                    
              
            elif bet_type == 'vip_264':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('speed_vip',code))
                state = self.room_264()
                room = data_room_nakee['records'][state]['id']
                
            elif bet_type == 'normal':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('yeekee',code))
                state = self.room_88()
                room = data_room_nakee['records'][state]['id']
                
          
            elif bet_type == 'vip_88':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('yeekee_vip',code))
                state = self.room_88()
                room = data_room_nakee['records'][state]['id']
                
            elif bet_type == 'zodiac':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('zodiac',code))
                state = self.room_88()
                room = data_room_nakee['records'][state]['id']
            
        elif this_host == 'movewinbet':
            if bet_type == 'special':
                start_number = 1  
                state = self.room_264_movewinbet()
                
            elif bet_type == 'normal':
                start_number = 1
                state = self.room_88()
            
            room = start_number+state    
              
        # exceptions
        if this_host == 'jetsada' or this_host == 'thailotto':
             
            if bet_type == 'normal':
                if room > 203:
                    room = room + 5
                    
        if this_host in  ['ruay','lottovip'] :
            if this_host == 'ruay':
                if bet_type == 'normal':
                    self.driver.get('https://www.ruay.com/member/lottery/yeekee')
                    sleep(3)
                    room = self.driver.execute_script('return document.getElementsByClassName("countdown")[0].id')
                    sleep(1)
                    state = self.room_88()
            elif this_host == 'lottovip':
                if bet_type == 'normal':
                    self.driver.get('https://www.lottovip.com/member/lottery/yeekee')
                    sleep(3)
                    link_url = self.driver.execute_script('return document.getElementsByClassName("col-6 col-sm-6 col-md-6 col-lg-3")[1].firstElementChild.href')
                    sleep(1)
                    link_url_list = link_url.split('/')
                    room = link_url_list[len(link_url_list)-1]
                    state = self.room_88()    
                
        print('done get room :',room,'state',state)
        return room , state
    
    
    def go_shoot_number(self, user, set_delay,test_setting,bet_type,get_af):   # 225k no.16-25
        code = self.session_data[user]['authorization']
        this_host = self.session_data[user]['host']
        set_time_start = (21600 + 2*60) * 1000000
        
        server_delay = float(self.session_data[user]['server_delay'])
        number_send = 0
        
        	
        if bet_type == 'zodiac':
            number_send = random.randint(1, 12)
        else:
            number_send = random.randint(10000, 99999)
            
            
        self.number_send = number_send 
        print('number_send',number_send)
        
        
        room , state = self.get_room(user)
        
        
        ##### set time to click number #########
        
        if this_host == 'jetsada':
            time_to_click = state*15+362
            set_time_start = (21600 + 2*60) * 1000000
            time_par_round = 15*60*1000000
        elif this_host == 'huay' and bet_type == 'normal':
            time_to_click = state*5+361
            set_time_start = (21600 + 1*60) * 1000000
            time_par_round = 5*60*1000000
        
        elif this_host == 'thailotto':
            if bet_type == 'special':
                time_to_click = state*5+361
                set_time_start = (21600 + 1*60) * 1000000
                time_par_round = 5*60*1000000
            elif bet_type == 'normal':
                time_to_click = state*15+362
                set_time_start = (21600 + 2*60) * 1000000
                time_par_round = 15*60*1000000
                
        elif this_host == 'nakee' or this_host == 'ltobet' :
            if bet_type == 'special' or bet_type == 'vip_264' :
                time_to_click = state*5+361
                set_time_start = (21600 + 1*60) * 1000000
                time_par_round = 5*60*1000000
            elif bet_type == 'normal' or bet_type == 'vip_88' or bet_type == 'zodiac' :
                time_to_click = state*15+362
                set_time_start = (21600 + 2*60) * 1000000
                time_par_round = 15*60*1000000
            
        elif this_host in ['ruay','lottovip']:
            if bet_type == 'special':
                time_to_click = state*5+361
                set_time_start = (21600 + 1*60) * 1000000
                time_par_round = 5*60*1000000
            elif bet_type == 'normal':
                time_to_click = state*15+362
                set_time_start = (21600 + 2*60) * 1000000
                time_par_round = 15*60*1000000    
            
        elif this_host == 'movewinbet':
            if bet_type == 'special':
                time_to_click = state*5+6
                set_time_start = (300 + 1*60) * 1000000
                time_par_round = 5*60*1000000
            elif bet_type == 'normal':
                time_to_click = state*15+362
                set_time_start = (21600 + 2*60) * 1000000
                time_par_round = 15*60*1000000
        
        if test_setting == True:
            test = time_par_round
        else:
            test = 0
            
        hour = int(time_to_click/60)
        minute = int(time_to_click % 60)
        
        if state < 0:
            print('can not bet yet')
            # return False
        else:
            print('start___BETTTT : %s' % str(this_host) )


                
                
        print(room)
        if this_host == 'jetsada':
            state_ref = 0
            _url = str('https://www.jetsada.net/member/lottery/yeekee/%s' % (room))
            if bet_type == "special":
                js_send_number = 'axios.post("/member/lottery/yeekee", {number: "%s", bet_category_id: %s, yeekee_special: "plus"});' % (str(number_send),str(room))
            elif bet_type == "normal":
                js_send_number = 'axios.post("/member/lottery/yeekee", {number: "%s", bet_category_id: %s, yeekee_special: ""});' % (str(number_send),str(room))
        
        elif this_host == 'huay':
            state_ref = 1
            _url = str('https://s1.huay.com/member#/lottery/yeekee/%s' % (room))
            js_send_number = 'axios.post("/protection/lottery/yeekee", { number: %s, bet_category_id: %s,main_type: 1}) ' % (str(number_send),str(room))
        
        elif this_host == 'thailotto':
            state_ref = 0
            _url = str('https://thailotto.io/member/lottery/yeekee/%s' % (room))
            
            # js_send_number = 'axios.post("/member/lottery/yeekee", {number: "%s", bet_category_id: %s, yeekee_special: ""});' % (str(number_send),str(room))
            js_send_number = str(js_code.post_number_jesadabet(code,room,number_send))
            self.driver.get('https://thailotto.io/member/affiliate')
            
        elif this_host == 'nakee':
            state_ref = 0
            _url = str('https://nakee.com/member/lotto/%s' % (room))
            js_send_number = str(js_code.post_number_nakee(code,room,number_send))
        
        elif this_host in ['ruay','lottovip']:
            state_ref = 0
            if this_host == 'ruay':
                
                _url = str('https://www.ruay.com/member/lottery/yeekee/%s' % (room))
                
                js_send_number = str(js_code.post_number_ruay(room,number_send,"https://www.ruay.com/Api/y_number"))
            elif this_host == 'lottovip':
                _url = str('https://www.lottovip.com/member/lottery/yeekee/%s' % (room))
                
                js_send_number = str(js_code.post_number_ruay(room,number_send,"https://www.lottovip.com/Api/y_number"))
        
        elif this_host == 'ltobet':
            state_ref = 0
            _url = str('https://nakee.com/member/lotto/%s' % (room))
            js_send_number = str(js_code.post_number_ltobet(code,room,number_send,bet_type))        
        
        elif this_host == 'movewinbet':
            state_ref = 0
            
            if bet_type == 'normal':
                type_url = 'yeekee'
            else:
                type_url = 'yeekee-vip'
                
                
            _url = str('https://%s/member/%s/%s' % (str(self.movewinbet_url) ,str(type_url) , str(room) ))
            js_send_number = str(js_code.post_number_movewinbet(room,number_send,self.movewinbet_url,bet_type))  
        
        # print(js_send_number)
        # self.driver.get(_url)
        sleep(2)
        self.driver.save_screenshot('pic_shot.png')
        self.room_url = _url
        self.room_number = room
        self.state = state
        sleep(1)
        
        
        
        if get_af > 100:
            js_send_number = ''
            
        use_time = 0
        rand_time = (30 + random.randint(0, 4))

        delay = (1000000-set_delay)/1000000
        
        try:
            if this_host == 'movewinbet':
                while(1):
                    now = datetime.datetime.now()
                    time_in_microsec = (
                        (now.hour*3600 + now.minute*60 + now.second)*1000000 + now.microsecond)
                    loop_time = (time_in_microsec - set_time_start)
                    
                    
                        
                    if (loop_time - server_delay*1000000) % time_par_round > time_par_round - 1000000 - test and state_ref == 1:
                        print('ckick to win')
                        sleep(delay)
                        try:
                            self.driver.execute_script(js_send_number) 
                            now = datetime.datetime.now()  
                            self.driver.execute_script(js_send_number) 
                            end = datetime.datetime.now()
                            self.driver.execute_script(js_send_number) 
                            
                            print('done : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now) )
                            use_time = (end-now).microseconds
                            self.use_time = use_time
                            
                        except:
                            pass
                        break
                    

                    if state_ref == 0 :
            
                        time_delay_movewin = 50
                            
                        if (loop_time - server_delay*1000000) % time_par_round > time_par_round - 1000000*time_delay_movewin - test:
                            
                            try:
                                print('ckick 1st')
                                sleep(0.01)
                                
                                now = datetime.datetime.now()  
                                self.driver.execute_script(js_send_number) 
                                end = datetime.datetime.now()  
                                
                                print('done ckick 1st :' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now))
                                sleep(11)
                                
                                #########################################
                                print('ckick 2nd')
                                sleep(0.01)
                                
                                
                                now = datetime.datetime.now()  
                                self.driver.execute_script(js_send_number) 
                                end = datetime.datetime.now()  
                                
                                print('done ckick 2nd : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now))
                                sleep(11)
                                
                                #########################################
                                print('ckick 3th')
                                sleep(0.01)
                                
                                
                                now = datetime.datetime.now()  
                                self.driver.execute_script(js_send_number) 
                                end = datetime.datetime.now()  
                                
                                print('done ckick 3th : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now))
                                sleep(11)
                            
                                #########################################
                                print('ckick 4th')
                                sleep(0.01)
                                
                                
                                now = datetime.datetime.now()  
                                self.driver.execute_script(js_send_number) 
                                end = datetime.datetime.now()  
                                
                                print('done ckick 4th : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now))
                                # sleep(11)
                                
                            except:
                                pass
                            
                            state_ref = 1
            
            else:
            
                while(1):
                    now = datetime.datetime.now()
                    time_in_microsec = (
                        (now.hour*3600 + now.minute*60 + now.second)*1000000 + now.microsecond)
                    loop_time = (time_in_microsec - set_time_start)
                    
                    
                        
                    if (loop_time - server_delay*1000000) % time_par_round > time_par_round - 1000000 - test and state_ref == 1:
                        print('ckick to win')
                        sleep(delay)

                        if this_host == 'thailotto':
                            self.driver.execute_script(js_send_number) 
                            # sleep(0.000001)
                        now = datetime.datetime.now()  
                        self.driver.execute_script(js_send_number) 
                        end = datetime.datetime.now()
                        if this_host == 'thailotto':
                            # sleep(0.000001)
                            self.driver.execute_script(js_send_number) 
                        
                        print('done : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now) )
                        use_time = (end-now).microseconds
                        self.use_time = use_time
                        break
                    

                    if state_ref == 0 :
                        if (loop_time - server_delay*1000000) % time_par_round > time_par_round - 1000000*rand_time - test:
                            try:
                                print('ckick 1st')
                                sleep(delay)
                                self.driver.refresh()
                                sleep(1.5)
                                # self.driver.save_screenshot('1150.png')
                                    
                                sleep(0.5)
                                
                                ######### ยิงเลขครั้งแรก ##############
                                
                                self.driver.execute_script(js_send_number) 
                                print('done ckick 1st')
                                sleep(1)
                                
                                self.driver.refresh()
                            except:
                                pass
                        
                            state_ref = 1
        except:
            pass
                
            
                
        sleep(0.1)
        # self.save_screenshots(user)

        print('end process shot number')
        
        
    def get_af_thailotto(self,user,balance):
        
        if ',' in balance:
            balance = balance.replace(",", "")
            
            
        price = int(int(int(float(balance))/100) - 2)
        
        print('bet price :'  + str(price))
        code = self.session_data[user]['authorization']

        room , state = self.get_room(user)
        
        if state < 0:
            print('can not bet yet')
            return False
        else:
            print('start___select')
            
        sleep(2)
        
        
        betListJsonStringify = '['
        for n in range(100):
            
            num = ""
            if n < 10 :
                num = str(0) + str(n)
            else:
                num = str(n)
                
            betListJsonStringify = betListJsonStringify + str(r'{\"type\":3,\"slug\":\"bet_two_top\",\"number\":\"%s\",\"price\":%s},' % (str(num),str(price)))
            
            
        count_n = len(betListJsonStringify)
        betListJsonStringify = list(betListJsonStringify)
        betListJsonStringify[count_n-1] = ']'
        betListJsonStringify = ''.join(betListJsonStringify)   

        bet_text = '{"stake_method":2,"bet_category_id":%s,"betListJsonStringify":"%s","thaistock20checklist":[]}' % (str(room),betListJsonStringify)
        js = js_code.bet_number_jesadabet(code,bet_text)
        sleep(2)
        self.driver.get('https://thailotto.io/member/affiliate')
        sleep(2)

        self.driver.execute_script(js)
    
        print('done bet number for get AF')



    def select_number(self,user,list_number,bet_type):
        print('select_number_process',datetime.datetime.now())
        
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        
        room , state = self.get_room(user)

        ###### set url for go shot number #########
            
        if state < 0:
            print('can not bet yet')
            return False
        else:
            print('start___select')
 
        
        sleep(2)


        # this_host == 'jetsada' or this_host == 'thailotto' or this_host == 'nakee':
        betListJsonStringify = '['

        # for n in list_number:
        for count, n in enumerate(list_number):
            num = ""
            if n < 10 and bet_type != 'zodiac':
                num = str(0) + str(n)
            else:
                num = str(n)
            
        
            
            if this_host == 'jetsada' or this_host == 'thailotto':
                betListJsonStringify = betListJsonStringify + str(r'{\"type\":3,\"slug\":\"bet_two_top\",\"number\":\"%s\",\"price\":2},' % (str(num)))
            
            # elif this_host == 'movewinbet':
            #     price = n
            #     number_bet = ""
            #     if count < 10:
            #         number_bet = str(0) + str(count)
            #     else:
            #         number_bet = str(count)
                
            #     if price > 0:
            #         betListJsonStringify = betListJsonStringify + str('{"s":"bet_two_top","n":"%s","p":"%s","r":90},' % (str(number_bet) , str(price)))
            
            
            elif this_host == 'movewinbet':
                price = 2
                number_bet = ""
                if n < 10:
                    number_bet = str(0) + str(n)
                else:
                    number_bet = str(n)
                
                if price > 0:
                    betListJsonStringify = betListJsonStringify + str('{"s":"bet_two_top","n":"%s","p":"%s","r":90},' % (str(number_bet) , str(price)))
                    
                
            elif this_host == 'nakee':
                price = 2

                if bet_type == 'special':
                    rate = 90
                elif bet_type == 'vip_264':
                    rate = 90
                elif bet_type == 'normal':
                    rate = 90
                elif bet_type == 'vip_88':
                    rate = 90
                    price = 10
                    
                betListJsonStringify = betListJsonStringify + str(r'{\"slug\":\"two_top\",\"number\":\"%s\",\"price\":\"%s\",\"rate\":\"%s\"},' % (str(num),str(price),str(rate)))
            
            elif this_host == 'ltobet':
                price = 2

                if bet_type == 'special':
                    rate = 90
                elif bet_type == 'vip_264':
                    rate = 90
                    price = 10
                elif bet_type == 'normal':
                    rate = 90
                elif bet_type == 'vip_88':
                    rate = 90
                    price = 10
                elif bet_type == 'zodiac':
                    rate = 10
                    price = 25
                
                if bet_type == 'zodiac':
                    betListJsonStringify = betListJsonStringify + str(r'{\"slug\":\"zodiac\",\"znumber\":\"%s\",\"number\":\"\",\"price\":\"%s\",\"rate\":\"%s\"},' % (str(num),str(price),str(rate)))
                else:
                    betListJsonStringify = betListJsonStringify + str(r'{\"slug\":\"two_top\",\"number\":\"%s\",\"price\":\"%s\",\"rate\":\"%s\"},' % (str(num),str(price),str(rate)))
            
        count_n = len(betListJsonStringify)
        betListJsonStringify = list(betListJsonStringify)
        betListJsonStringify[count_n-1] = ']'
        betListJsonStringify = ''.join(betListJsonStringify)

        if this_host == 'jetsada' or this_host == 'thailotto':
            bet_text = '{"stake_method":2,"bet_category_id":%s,"betListJsonStringify":"%s","thaistock20checklist":[]}' % (str(room),betListJsonStringify)
            js = js_code.bet_number_jesadabet(code,bet_text)
            sleep(2)
            self.driver.get('https://thailotto.io/member/affiliate')
            sleep(2)
            
        elif this_host == 'movewinbet':
            if bet_type == 'normal':
                type_url = 'yeekee'
            else:
                type_url = 'yeekee-vip'
            
            movewinbet_url_bet = "https://%s/member/%s/%s" % (str(self.movewinbet_url) , str(type_url) , str(room) )
            
            
            self.driver.get(movewinbet_url_bet)
            sleep(3)
            print('bet web : ' + str(movewinbet_url_bet))
            bet_url = self.driver.execute_script('return betUrl')
            print(bet_url)
            js = js_code.bet_number_movewinbet(room,betListJsonStringify,bet_url)
            sleep(2)
            self.driver.get('https://%s/member/affiliate' % str(self.movewinbet_url))
            sleep(2)
        
        elif this_host == 'nakee':
            hash = random.getrandbits(128)
            link = ''
            if bet_type == 'special':
                link = 'speed'
            elif bet_type == 'vip_264':
                link = 'speed_vip'
            elif bet_type == 'vip_88':
                link = 'yeekee_vip'
            elif bet_type == 'normal':
                link = 'yeekee'
            
                
            bet_text = '{"lotto_id":%s,"stakes":"%s","hashed":"%s"}' % (str(room),betListJsonStringify,str(hash))
            js = js_code.bet_number_nakee(code,link,bet_text)
            sleep(2)
            self.driver.get('https://nakee.com/member/affiliate')
            sleep(2)
        
        elif this_host == 'ltobet':
            hash = random.getrandbits(128)
            link = ''
            if bet_type == 'special':
                link = 'speed'
            elif bet_type == 'vip_264':
                link = 'speed_vip'
            elif bet_type == 'vip_88':
                link = 'yeekee_vip'
            elif bet_type == 'normal':
                link = 'yeekee'
            elif bet_type == 'zodiac':
                link = 'zodiac'
                
            bet_text = '{"lotto_id":%s,"stakes":"%s","hashed":"%s"}' % (str(room),betListJsonStringify,str(hash))
            js = js_code.bet_number_ltobet(code,link,bet_text)
            sleep(2)
            self.driver.get('https://www.ltobet.com/member/affiliate')
            sleep(2)
        
        self.driver.save_screenshot('bet_number.png')
        self.driver.execute_script(js)
    
       
        
        print('done bet number')


    def get_balance(self,user):
        
        print('do process get_balance')
        
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        point = 0
        if this_host == 'thailotto' or this_host == 'jetsada':
            _url = 'https://thailotto.io/member/clear-credit-cache/' + str(self.session_data[user]['ID'])
            self.driver.get(_url)
            sleep(1)
            # self.driver.save_screenshot('11111.png')

            balance = self.driver.execute_script("return document.body.innerText")

            sleep(2)

            self.driver.get('https://thailotto.io/member/game')

            sleep(2)
            
            point = self.driver.execute_script("return document.getElementsByClassName('font-xl text-success')[0].innerText")
            
            
        if this_host == 'movewinbet':
            _url = 'https://%s/member/get-credit?auto_update_credit=0' % str(self.movewinbet_url) 
            self.driver.get(_url)
            sleep(1)
            # self.driver.save_screenshot('11111.png')

            balance = self.driver.execute_script("return document.body.innerText")
        
        elif this_host == 'nakee':
            balance = self.driver.execute_script(str(js_code.get_balance_nakee(code)))['data']['real_credit']
        
        elif this_host == 'lottovip':
            self.driver.get('https://www.lottovip.com/member/credit_balance')
            
            balance = self.driver.execute_script("return document.body.innerText")
            
        elif this_host == 'ruay':
            self.driver.get('https://www.ruay.com/member/credit_balance')
            
            balance = self.driver.execute_script("return document.body.innerText")
        
        elif this_host == 'ltobet':
            balance = self.driver.execute_script(str(js_code.get_balance_ltobet(code)))['data']['real_credit']
            if balance == "not have wallet":
                balance = 0.00
                
                
        return balance , point

    def stop_display(self):
        self.display.stop()

    def save_screenshots(self, user):
        now = datetime.datetime.now()
        try:
            self.session_data[str(user)]['driver'].save_screenshot(
                str(file_part) + 'scr/' + str(user) + "_" + str(now) + ".png")

            print('done save  :  ' + str(user) + '\t' + str(now))
        except:
            print('not find user  :' + user)
            

if __name__ == "__main__":
    
    a = subprocess.call("pkill chrome", shell=True)
    a = subprocess.call("pkill Xvfb", shell=True)
    # sleep(random.randint(0,150)/10)
    
    try:
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        
        if time_in_minute > 355 or time_in_minute < 240:
            print('bot is doing there job right now!!!')
        else:
            print('Not in time')
            # exit()
        
        data_json = {'ip': external_ip , 'host' : 'jetsada'  ,'process' : 'get_user' }
        sleep(random.randint(0, 30)/10)
        data_get = json.loads(requests.post('http://128.199.236.187:8888/jesadabet/get_id',data=data_json ,timeout=60).text)
        # json_user = json.dumps(data.text)
        
        print(data_get)
        data = data_get['data']
        print(data)
        
        
        codename = str(list(data.keys())[0])
        time_delay = int(data[codename]['time_delay'])
        username = data[codename]['ID']
        
        bet_type = data[codename]['bet_type'] 
        
        
        if data[codename]['test'] == 'yes':
            test_process = True
        else:
            test_process = False
            

        # if data[codename]['host'] in ['jetsada' , 'thailotto' , 'nakee', 'ruay' , 'lottovip' ] : 
        if 1 == 1 :
            class_obj = yeekee_bot(data)
            
            
            a = subprocess.call("pkill chrome", shell=True)
            sleep(2)
            r = class_obj.create_connection()
                
                
            start = int(data[codename]['start'])
            end = int(data[codename]['end'])+1
            sleep(2)
            
            get_af = int(data[codename]['get_af'])
            
            
            
            if get_af > 100 and data[codename]['host'] == 'thailotto':
                balance , point = class_obj.get_balance(codename)
                class_obj.get_af_thailotto(codename,balance)
                sleep(10) 
                class_obj.go_shoot_number(codename, time_delay,test_process,bet_type,get_af)
                sleep(40)
              
            
            else : 
                
                #### เลือกเลข ####
                # if data[codename]['host'] == 'movewinbet':
                if data[codename]['host'] == 'bra bra bra':
                    # n_bet = random.randint(50, 51)
                    n_bet = 50
                    l = []
                    for i in range(100):
                        l.append(0)
                    for i in range(n_bet):
                        _n = random.randint(0, 99)
                        l[_n] = l[_n] + 2
                
                else:
                    l = [i for i in range(start,end)]
                    
                if data[codename]['use_money'] == 'yes':
                    class_obj.select_number(codename,l,bet_type=bet_type)


                #### ยิงเลข ####
                class_obj.go_shoot_number(codename, time_delay,test_process,bet_type,get_af)
                sleep(10)
                try:
                    class_obj.get_bonus_vip(codename,data[codename]['host'])
                except:
                    pass
                
                sleep(10)
            
            
            #### เช็ค balance ล่าสุด ####
            
            
            
            balance , point = class_obj.get_balance(codename)
        
            sleep(5)
            
            print('balance  :' + str(balance) )
            sleep(10)
            if get_af > 100:
                rank = 0
                number_shot = 99999
                bonus = 0
               
            else:
                rank = class_obj.get_result(codename,bet_type)
                number_shot = class_obj.number_send
                bonus = class_obj.bonus
            sleep(2)
            print('rank :' + str(rank))
            
            
            
            host = data[codename]['host'] 
            
          
            room_number = int(class_obj.state) + 1
            
            day_start_bet = (datetime.datetime.now() - datetime.timedelta(hours=5)).date()
            
            print('start send data')
            
            
            data_json = {'username' : username ,
                        'host' : data[codename]['host'] , 
                        'bet_type' : data[codename]['bet_type'] ,
                        'delay_use' : time_delay ,
                        'time_use' : class_obj.use_time,
                        'date' : day_start_bet , 
                        'bet_round' : room_number , 
                        'rank' : rank , 
                        'balance' : balance ,
                        'version' : version_yeekee ,
                        'bonus' : bonus ,
                        'number_shot' : number_shot ,
                        'get_af' : get_af ,
                        'point' : point , 
                        'server_delay' : data[codename]['server_delay'] 
                        }
            print(data_json)
            time_num = random.randint(0, 10)/10
            
            if int(rank) == 0:
                time_num = time_num + 8
                
            time.sleep(time_num)
            
            r = requests.post('http://128.199.236.187:8888/jesadabet/send_history',data=data_json)
            print(r.status_code)
            class_obj.driver.quit()
            class_obj.stop_display()
                
                
                
                
    except Exception as e :
        print(e)
        
        
    sleep(2)    
    a = subprocess.call("pkill chrome", shell=True)
    print('done')
    sleep(2)
    exit()

