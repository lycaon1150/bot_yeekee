
import datetime

import random
# import sched
import subprocess
import sys
import time
from typing import Tuple
from webbrowser import get
import requests
import json
import threading
import math
import sys 
import shutil
from time import sleep


import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
import js_code
import os

file_part = os.path.dirname(os.path.realpath(__file__))
version_yeekee = "v2.15b"
print(datetime.datetime.now())
target_F = ""
log_out = ""

print(version_yeekee)


class yeekee_bot(object):
    def __init__(self, json_user):
        self.json_user = json_user
        self.session_data = {}
        self.room_url_special = ""
        self.room_url_normal = ""
        self.room_number_special = ""
        self.room_number_normal = ""
        self.state_special = ""
        self.state_normal = ""
        self.use_time_special = 0
        self.use_time_normal = 0
        self.number_send_special = ""
        self.number_send_normal = ""
        
        self.driver = ''
        self.bonus = 0
        self.display = Display(visible=0, size=(800, 800)) 
        self.movewinbet_url = ""
        self.mungmeelt_uid = ""
        self.last_rank_special  = 0
        self.last_rank_normal  = 0
        self.rank_special  = 0
        self.rank_normal  = 0
        
        self.last_rank_b = 150
        
        print('success created')
    
    def launchBrowser(self,server,host):
        options = uc.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-web-security")
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
        for user in self.json_user.keys():
            data_id = self.json_user[user]

            self.launchBrowser(data_id['sever'],data_id['host'])
              
            json_data = data_id
            
            # self.driver.get('https://api.ipify.org')
            # sleep(1)
            # self.driver.save_screenshot('pic_ip.png')
            # json_data['driver'] = driver
            json_data['authorization']  = ''
            self.driver.delete_all_cookies()
            
            try:
                sleep(0.5)
                json_data['authorization'] = self.login( json_data['host'],json_data['ID'], json_data['Password'], json_data['url'])
                sleep(0.5)
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
        sleep(1)
        self.driver.save_screenshot('pic_home.png')
        print(self.driver.execute_script('return navigator.webdriver'))
        
        
        if host in [ 'jetsada' , 'huay' , 'thailotto' , 'ruay' , 'lottovip' ]:
            
            if host == 'jetsada':
                self.driver.execute_script("document.getElementsByClassName('btn btn-bar btn-border btn-login-modal')[0].click();")
                class_username = 'username'
                sleep(0.5)
            elif host == 'thailotto':
                # self.driver.execute_script("document.getElementsByClassName('btn btn-bar btn-login-modal')[0].click();")
                sleep(0.5)
                
            self.driver.execute_script("document.getElementsByName('username')[0].value='%s';" % str(id))
            self.driver.execute_script("document.getElementsByName('password')[0].value='%s';" % str(pwd))
            sleep(0.5)
            
            if host in [ 'jetsada' , 'huay' , 'thailotto' ] :
            
                self.driver.execute_script("document.querySelectorAll('button[type=submit]')[1].click();")
                sleep(0.5)
                r = self.driver.execute_script("return (await window.cookieStore.get('XSRF-TOKEN')).value")
            
            elif host in  ['ruay','lottovip'] :
                
                self.driver.execute_script("document.querySelectorAll('button[type=submit]')[0].click();")
                sleep(1)
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
                
        sleep(1)
        self.driver.save_screenshot('pic_login.png')
        return r    
       
    def get_room(self,user,this_host,bet_type):
        print('get_room')
        code = self.session_data[user]['authorization']
    
        
        start_number = 0
        state = 0 
        
        if this_host == 'huay':
            if bet_type == 'normal':
                state = self.room(88)
                start_number = 161
            elif bet_type == 'special':
                state = self.room(264)
                start_number = 514
        
        elif this_host == 'thailotto':
            if bet_type == 'special':
                start_number = 450  
                state = self.room(264)
                
            elif bet_type == 'normal':
                start_number = 172
                state = self.room(88)
            
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
                state = self.room(264)

            elif bet_type == 'vip_264':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 1701:
                        start_number = int(item['id'])
                        break
                state = self.room(264)
                
            elif bet_type == 'normal':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 101:
                        start_number = int(item['id'])
                        break
                
                state = self.room(88)
            
            elif bet_type == 'vip_88':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 201:
                        start_number = int(item['id'])
                        break
                    
                state = self.room(88)
            
            elif bet_type == 'speed_double':
                for item in data_room_nakee['records']:
                    if item['category_id'] == 3501:
                        start_number = int(item['id'])
                        break
                state = self.room(264)
                
            room = start_number+state 
            
        elif this_host == 'ltobet':
            
            data_room_nakee = ""
            attempts = 0
      
            if bet_type == 'special':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('speed',code))
                state = self.room(264)
                room = data_room_nakee['records'][state]['id']
                    
              
            elif bet_type == 'vip_264':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('speed_vip',code))
                state = self.room(264)
                room = data_room_nakee['records'][state]['id']
                
            elif bet_type == 'normal':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('yeekee',code))
                state = self.room(88)
                room = data_room_nakee['records'][state]['id']
                
          
            elif bet_type == 'vip_88':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('yeekee_vip',code))
                state = self.room(88)
                room = data_room_nakee['records'][state]['id']
                
            elif bet_type == 'zodiac':
                data_room_nakee = self.driver.execute_script(js_code.get_room_ltobet('zodiac',code))
                state = self.room(88)
                room = data_room_nakee['records'][state]['id']
            
        elif this_host == 'movewinbet':
            if bet_type == 'special':
                start_number = 1  
                state = self.room(288)
                
            elif bet_type == 'normal':
                start_number = 1
                state = self.room(88)
            
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
                    state = self.room(88)
            elif this_host == 'lottovip':
                if bet_type == 'normal':
                    self.driver.get('https://www.lottovip.com/member/lottery/yeekee')
                    sleep(3)
                    link_url = self.driver.execute_script('return document.getElementsByClassName("col-6 col-sm-6 col-md-6 col-lg-3")[1].firstElementChild.href')
                    sleep(1)
                    link_url_list = link_url.split('/')
                    room = link_url_list[len(link_url_list)-1]
                    state = self.room(88)    
                
        print('done get room :',room,'state',state)
        return room , state
       
    def room(self,max_room):
        now = datetime.datetime.now()
        if max_room == 88:
            time_in_minute = (now.hour*60 + now.minute)
            if time_in_minute < 240:
                state = int((time_in_minute-347+1440)/15)
            else:
                state = int((time_in_minute-347)/15)
            return state
    
        elif max_room == 264:
            time_in_minute = (now.hour*60 + now.minute)
            if time_in_minute < 240:
                state = int((time_in_minute-356+1440)/5)
            else:
                state = int((time_in_minute-356)/5)
            return state
    
        elif max_room == 288:
            now = datetime.datetime.now()
            time_in_minute = (now.hour*60 + now.minute)
            state = int((time_in_minute)/5)
            return state
    
    def select_number(self,user,list_number,bet_type,room,state):
        print('select_number_process',datetime.datetime.now())
        
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        
        # room , state = self.get_room(user)

        ###### set url for go shot number #########
            
        if state < 0:
            print('can not bet yet')
            return False
        else:
            print('start___select')
 
        
        sleep(2)


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
            
            elif this_host == 'movewinbet':
                if bet_type == "special":
                    price = 0
                else:
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
                
                if bet_type == 'speed_double':
                    rate = 95
                else:
                    rate = 90
              
                    
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
            sleep(0.5)
            self.driver.get('https://lotto5555.com/member/affiliate')
            sleep(0.5)
            
        elif this_host == 'movewinbet':
            if bet_type == 'normal':
                type_url = 'yeekee'
            else:
                type_url = 'yeekee-vip'
            
            
            
            movewinbet_url_bet = "https://%s/member/%s/%s" % (str(self.movewinbet_url) , str(type_url) , str(room) )
            
            
            self.driver.get(movewinbet_url_bet)
            sleep(3)
            print('bet web : ' + str(movewinbet_url_bet))
            bet_url = "https://%s/member/%s/%s/bet?userId=1150" % (str(self.movewinbet_url) , str(type_url) , str(room) )
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
            elif bet_type == 'speed_double':
                link = 'speed_double'
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
        try:
            print(bet_type)
            output = self.driver.execute_script(js)
            print(output)
            
        except:
            pass
       
        
        print('done bet number')

    def go_shoot_number(self, user, set_delay,test_setting,bet_type,room,state,money):   # 225k no.16-25
        code = self.session_data[user]['authorization']
        this_host = self.session_data[user]['host']
        set_time_start = (21600 + 2*60) * 1000000
        
        server_delay = float(self.session_data[user]['server_delay'])
        number_send = 0
        
        	
        if bet_type == 'zodiac':
            number_send = random.randint(1, 12)
        else:
            number_send = random.randint(10000, 99999)
            
        print('bet type  : ' + bet_type )
        print('number_send',number_send)
        
        
        if bet_type == 'normal':
      
            self.number_send_normal = number_send 
        else:
         
            self.number_send_special = number_send 
        
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
            if bet_type == 'special' or bet_type == 'vip_264' or bet_type ==  'speed_double':
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
            _url = str('https://lotto5555.com/member/lottery/yeekee/%s' % (room))
            
            # js_send_number = 'axios.post("/member/lottery/yeekee", {number: "%s", bet_category_id: %s, yeekee_special: ""});' % (str(number_send),str(room))
            js_send_number = str(js_code.post_number_jesadabet(code,room,number_send))
            
            # js_send_number = str(js_code.post_multitime_thailotto(code,room,number_send))
            
            self.driver.get('https://lotto5555.com/member/affiliate')
            
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
            
            # js_send_number = str(js_code.post_number_movewinbet(room,number_send,self.movewinbet_url,bet_type))  
            js_send_number = str(js_code.post_multitime_number_movewinbet(room,number_send,self.movewinbet_url,bet_type)) 
        # print(js_send_number)
        self.driver.get(_url)
        
        sleep(2)
        self.driver.save_screenshot('pic_shot.png')
        if bet_type == "normal":
            self.room_url_normal = _url
        else:
            self.room_url_special = _url
        # self.room_number = room
        # self.state = state
        sleep(1)
        print(_url)
        # if get_af > 100:
        #     js_send_number = ''
            
        use_time = 0
        if this_host == 'movewinbet':
            rand_time = (68 + random.randint(50, 200)/100)
        elif this_host == 'thailotto' and bet_type == 'normal':
            # rand_time = (34 + random.randint(50, 300)/100)
            rand_time = 18+17
        else:
            rand_time = (20 + random.randint(50, 200)/100)

        delay = (1000000-set_delay)/1000000
        
        try:
            
            server_delay_sec = int(server_delay*1000000)
            time_set_round = time_par_round - 1000000 - test
            while(1):
                now = datetime.datetime.now()
                
                # if now.minute in [13,14,15,16,28,29,30,31,43,44,45,46,58,59,0,1] and data[codename]['host'] == 'movewinbet' and bet_type != 'normal':
                #     self.use_time_special = 0
                #     break
                        
                if state_ref == 1 and now.second == 58:
                    sleep(0.9985)
                # if (loop_time - server_delay_sec) % time_par_round > time_set_round and state_ref == 1:
                    print('ckick to win')
                    print(delay)
                    sleep(delay)
                    
                    if this_host == 'thailotto' and bet_type == 'normal' and money == 'no':
                        pass
                    else:
                        now = datetime.datetime.now()  
                        res = self.driver.execute_script(js_send_number) 
                        end = datetime.datetime.now()
                    print(res)
    
                    
                    print('done : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now) )
                    use_time = (end-now).microseconds
                    if bet_type == 'normal':
                        self.use_time_normal = use_time
                    else:
                        self.use_time_special = use_time
                    break
                
                time_in_microsec = (
                    (now.hour*3600 + now.minute*60 + now.second)*1000000 + now.microsecond)
                loop_time = (time_in_microsec - set_time_start)
                
                if state_ref == 0 :
                    if (loop_time - server_delay*1000000) % time_par_round > time_par_round - 1000000*rand_time - test:
                        try:
                            print('ckick 1st')
                            # sleep(delay)
                            # self.driver.refresh()

                                
                            sleep(2.5)
                            
                            ######### ยิงเลขครั้งแรก ##############
                            if money == 'yes':
                                now = datetime.datetime.now() 
                                self.driver.execute_script(js_send_number) 
                                print('done ckick 1st')
                                print(now)
                                sleep(2.2)
                                self.driver.refresh()
                            elif this_host == 'thailotto' and bet_type == 'normal' and money == 'no':
                                sleep(25)
                                now = datetime.datetime.now() 
                                if room < 235 or (room > 253 and room < 265):
                                    self.driver.execute_script(js_send_number) 
                                print('done ckick 1st')
                                print(now)
                                sleep(2)
                                self.driver.refresh()
                            
                            if this_host == 'thailotto' and bet_type == 'normal' and money == 'yes':
                                sleep(16-2.2)
                                now = datetime.datetime.now() 
                                self.driver.execute_script(js_send_number) 
                                print('done ckick 1st')
                                print(now)
                                sleep(2.2)
                                self.driver.refresh()
                                    
                            # ######### ยิงเลขครั้ง 2 movewin ##############
                            # if this_host == 'movewinbet':
                            #     for _i in range(4):
                            #         sleep(12)
                            #         now = datetime.datetime.now() 
                            #         self.driver.execute_script(js_send_number) 
                            #         print('done ckick ',_i+2)
                            #         print(now)
                            #         sleep(1)
                                
                            # if this_host == 'thailotto' and bet_type == 'normal':
                                
                            #     sleep(16)
                            #     now = datetime.datetime.now() 
                            #     self.driver.execute_script(js_send_number) 
                            #     print('done ckick ',_i+2)
                            #     print(now)
                            #     sleep(1)
                            
                       
                            
                            self.driver.refresh()
                            
                            
                            
                            
                        except Exception as e:
                            print('error shot number ckick 1st')
                            print(e)
                    
                        state_ref = 1
                        
        except Exception as e:
            print('error shot number')
            print(e)
                
            
                
        sleep(0.1)
        # self.save_screenshots(user)

        print('end process shot number')
        
    def get_result(self,user,bet_type):
        print('do process get_result')
        print('get rank')
        
        if bet_type == "normal":
            room_url = self.room_url_normal
            room_number = self.room_number_normal
            number_send = self.number_send_normal
        else:
            room_url = self.room_url_special
            room_number = self.room_number_special
            number_send = self.number_send_special
       
                
        print(room_url)
        print(room_number)
        # _url = str('https://www.jetsada.net/member/lottery/yeekee/%s' %(start_number+state))

        tries = 5
        for it in range(tries):
            try:
                self.driver.get(room_url)
            except KeyError as e:
                if it < tries - 1: # i is zero indexed
                    continue
                else:
                    raise
            break
        
        
        
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        sleep(1)
        self.driver.save_screenshot('rank.png')
        
        now = datetime.datetime.now()
        name = user.split("_")[1]
        print(name)
        secret_name = ""
        print(datetime.datetime.now())
        if bet_type == 'special' and now.minute in [2,17,32,47]:
            past_time = list(str(datetime.datetime.now()- datetime.timedelta(0,120)).split(".")[0])
        else:
            past_time = list(str(datetime.datetime.now()- datetime.timedelta(0,60)).split(".")[0])
            
        past_time[17] = "5"
        past_time[18] = "9"
        time_rank = str("".join(past_time)).split(" ")[1]
        print(time_rank)

        if this_host == 'jetsada' or this_host == 'thailotto':
            n = 0
            
            self.driver.get(room_url)
            for c in name:
                if n == 3 or n == 4 or n == 5:
                    secret_name = str(secret_name) + str('*')
                else:
                    secret_name = str(secret_name) + str(c) 
                n = n + 1
            print(secret_name)

            try:
                if bet_type == 'normal':
                    js_100 = """return document.querySelectorAll("a[href='?page=2&scrollToRow=50']")[0].innerText"""
                    name_100 = str(self.driver.execute_script(js_100))
                    if name_100 == name or name_100 == secret_name:
                        return 100
                elif bet_type == 'special':
                    js_50 = """return document.querySelectorAll("a[data-href='#row-50']")[0].innerText"""
                    name_50= str(self.driver.execute_script(js_50))
                    if name_50 == name or name_50 == secret_name:
                        return 50
                    
            except Exception as e:
                print(e)
        
            for i in range(50):
                js = "return document.getElementsByClassName('username')[%s].innerText" %i 
                js_time = "return document.getElementsByClassName('date')[%s].innerText" %i 
                
                last_rank_js = str(self.driver.execute_script(js_time)).split(" ")[1]
                
                if time_rank == last_rank_js:
                    if bet_type == "normal":
                        self.last_rank_normal = i+1
                    else:
                        self.last_rank_special = i+1


                find_name = self.driver.execute_script(js)
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1
            
           
            new_url = room_url + '?page=2'    
            self.driver.get(new_url)
            sleep(0.5)
        
            for i in range(50):
                js = "return document.getElementsByClassName('username')[%s].innerText" %i
                js_time = "return document.getElementsByClassName('date')[%s].innerText" %i 
                
                last_rank_js = str(self.driver.execute_script(js_time)).split(" ")[1]

                if time_rank == last_rank_js:
                    if bet_type == "normal":
                        self.last_rank_normal = i+51
                    else:
                        self.last_rank_special = i+51

                find_name = self.driver.execute_script(js)
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+51
                
                
            new_url = room_url + '?page=3'    
            self.driver.get(new_url)
            sleep(0.5)
        
            for i in range(50):
                js = "return document.getElementsByClassName('username')[%s].innerText" %i
                js_time = "return document.getElementsByClassName('date')[%s].innerText" %i 
                
                last_rank_js = str(self.driver.execute_script(js_time)).split(" ")[1]

                if time_rank == last_rank_js:
                    if bet_type == "normal":
                        self.last_rank_normal = i+101
                    else:
                        self.last_rank_special = i+101
                    
                find_name = self.driver.execute_script(js)
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+101
            
            new_url = room_url + '?page=4'    
            self.driver.get(new_url)
            sleep(0.5)
        
            for i in range(50):
                js = "return document.getElementsByClassName('username')[%s].innerText" %i
                js_time = "return document.getElementsByClassName('date')[%s].innerText" %i 
                
                last_rank_js = str(self.driver.execute_script(js_time)).split(" ")[1]

                if time_rank == last_rank_js:
                    if bet_type == "normal":
                        self.last_rank_normal = i+151
                    else:
                        self.last_rank_special = i+151
                    
                find_name = self.driver.execute_script(js)
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+151
        
        
        if this_host == 'movewinbet':
            n = 0

            sleep(10)
            self.driver.get(room_url)
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
                js_time = "return document.getElementsByClassName('number')[%s].innerText" % str(i*3+9) 
                
                last_rank_js = str(self.driver.execute_script(js_time)).split(" ")[1]
                
                if time_rank == last_rank_js:
                    if bet_type == "special":
                        
                        self.last_rank_special = i+1
                    else:
                        self.last_rank_normal  = i+1
                    
                    
                    
                    
                find_name = self.driver.execute_script(js).split('\n')[1]
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1
            
            sleep(0.5)
            new_url = room_url + '?page=2'    
            self.driver.get(new_url)
        
        
            for i in range(20):
                js = "return document.getElementsByClassName('item-col col-4 col-xl-4')[%s].innerText" % str(i*3+1)
                js_time = "return document.getElementsByClassName('number')[%s].innerText" % str(i*3+9) 
                
                last_rank_js = str(self.driver.execute_script(js_time)).split(" ")[1]
                
                if time_rank == last_rank_js:
                    if bet_type == "special":
                        
                        self.last_rank_special = i+21
                    else:
                        self.last_rank_normal = i+21
                    
                
                find_name = self.driver.execute_script(js).split('\n')[1]
                
                
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1+20
            
            
            sleep(0.5)
            new_url = room_url + '?page=3'    
            self.driver.get(new_url)
        
        
            for i in range(20):
                js = "return document.getElementsByClassName('item-col col-4 col-xl-4')[%s].innerText" % str(i*3+1)
                js_time = "return document.getElementsByClassName('number')[%s].innerText" % str(i*3+9) 
                
                last_rank_js = str(self.driver.execute_script(js_time)).split(" ")[1]
                
                if time_rank == last_rank_js:
                    if bet_type == "special":
                        
                        self.last_rank_special = i+41
                    else:
                        self.last_rank_normal = i+41
                    
                    
                find_name = self.driver.execute_script(js).split('\n')[1]
                
                
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1+40
            
            sleep(0.5)
            
            new_url = room_url + '?page=4'    
            self.driver.get(new_url)
        
             
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
            
            
                
            
            result = []
            number = []
            
            if bet_type == 'zodiac':
                max_room = 2
                reward_list = list(self.driver.execute_script(str(js_code.get_rank_ltobet(code,room_number,1,bet_type)))['userRewards'])
           
                for json_item in reward_list:
                    print(json_item)
                    if str(secret_name) == str(json_item['username']) and str(number_send) == str(json_item['number']):
                        self.bonus = json_item['reward']
                        
            else:
                max_room = 4
            
            print('bonus : ' + str(self.bonus))
            
            for i in range(1,max_room):
                _r = list(self.driver.execute_script(str(js_code.get_rank_ltobet(code,room_number,i,bet_type)))['records'])
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
  
            result = []
            number = []
            created_at = []
            
            bonus_result =[]
            bonus_number =[]
            bonus_reward = []
            
            
            _bonus_data = list(self.driver.execute_script(str(js_code.get_bonus_nakee(code,room_number)))['userRewards'])
            
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
                _r = list(self.driver.execute_script(str(js_code.get_rank_nakee(code,room_number,i)))['records'])
                # print(_r)
                sleep(0.3)
                for data in _r:
                    
                    number.append(data['number'])
                    result.append(data['username'])
                    created_at.append(str(data['created_at']))

           
            for rank , username in enumerate(result):
                if time_rank == created_at[rank].split(" ")[1]:
                    if bet_type == "normal":
                        self.last_rank_normal = i+1
                    else:
                        self.last_rank_special = i+1
                
                if str(secret_name) == str(username) and str(number_send) == str(number[rank]):
                    return rank+1
        
        elif this_host in  ['ruay','lottovip'] :
            print('wait 120 sec for get Rank')
            sleep(120)
            for i in range(1,4):
                _url_ruay = room_url + "/" + str(i)
                self.driver.get(_url_ruay)
                sleep(2)
                for j in range(20):
                    if str(number_send) == str(self.driver.execute_script("return document.getElementsByClassName('mb-0')[%s].textContent" % str(j))):
                        return (i-1)*20 + j+1
            
            
            
        print('end process get_result')
        return 0        

    def get_balance(self,user):
        
        print('do process get_balance')
        
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        point = 0
        if this_host == 'thailotto' or this_host == 'jetsada':
            
            try:
                self.driver.get('https://lotto5555.com/member/game')

                sleep(1)
                
                point = str(self.driver.execute_script("return document.getElementsByClassName('font-xl text-success')[0].innerText"))
                if ',' in point:
                    point = point.replace(",", "")
                
                point = int(point)
                
                sleep(1)
                
            except:
                pass
            
            _url = "https://lotto5555.com/member/credit"
            
            tries = 5
            for it in range(tries):
                try:
                    self.driver.get(_url)
                except KeyError as e:
                    if it < tries - 1: # i is zero indexed
                        continue
                    else:
                        raise
                break
            sleep(1)
            
            balance = self.driver.execute_script("return document.getElementsByClassName('font-xl float-right')[0].textContent")    
            # sleep(2)
            
            
        if this_host == 'movewinbet':
            _url = 'https://%s/member/get-credit?auto_update_credit=0' % str(self.movewinbet_url) 
            self.driver.get(_url)
            sleep(1)
            

            balance = self.driver.execute_script("return document.body.innerText")
        
        elif this_host == 'nakee':
            tries = 5
            for it in range(tries):
                try:
                    balance = self.driver.execute_script(str(js_code.get_balance_nakee(code)))['data']['real_credit']
                except KeyError as e:
                    if it < tries - 1: # i is zero indexed
                        continue
                    else:
                        raise
                break
           
        
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
                
        print('done get balance')   
        print(balance)     
        print('point : ' + str(point))
        return balance , point

    def get_af_thailotto(self,user,balance):
        
        if ',' in balance:
            balance = balance.replace(",", "")
            
  
        price = int(int(int(float(balance))/100) - 2)
        
        print('bet price :'  + str(price))
        code = self.session_data[user]['authorization']

        room , state = self.get_room(user,'thailotto','special')
        
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
        self.driver.get('https://lotto5555.com/member/affiliate')
        sleep(2)

        self.driver.execute_script(js)
    
        print('done bet number for get AF')
    
    def get_af_nakee(self,user,balance):
        # if ',' in balance:
        #     balance = balance.replace(",", "")

        # if ' ' in balance:
        #     balance = balance.replace(" ", "")
        print('get_af_nakee')
        print('balance AF = ' , balance)    
        # price = int(int(int(int(balance/100))) - 0)
        price = math.floor(balance/100)
        print('bet price :'  + str(price))

        
        code = self.session_data[user]['authorization']

        room , state = self.get_room(user,'nakee','special')
        
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
                
            betListJsonStringify = betListJsonStringify + str(r'{\"slug\":\"two_top\",\"number\":\"%s\",\"price\":\"%s\",\"rate\":\"%s\"},' % (str(num),str(price),str(90)))
            
            
        count_n = len(betListJsonStringify)
        betListJsonStringify = list(betListJsonStringify)
        betListJsonStringify[count_n-1] = ']' 
        betListJsonStringify = ''.join(betListJsonStringify)   
        hash = random.getrandbits(128)

        bet_text = '{"lotto_id":%s,"stakes":"%s","hashed":"%s"}' % (str(room),betListJsonStringify,str(hash))
        js = js_code.bet_number_nakee(code,'speed',bet_text)
        sleep(2)
        self.driver.get('https://nakee.com/member/affiliate')
        sleep(2)
    

        self.driver.execute_script(js)
    
        print('done bet number for get AF')
        
    def get_bonus_vip(self,user,host):
        slot_machine = 0
        try:
            if host == "thailotto":
                
                self.driver.execute_script(js_code.post_bonus_thailotto())
                sleep(2)
                self.driver.get("https://lotto5555.com/member/game/lucky-box")
                sleep(2)
                slot_machine = int(self.driver.execute_script("return document.getElementsByClassName('slotwrapper m-auto')[0].innerText[0]"))*10000
                slot_machine = slot_machine + int(self.driver.execute_script("return document.getElementsByClassName('slotwrapper m-auto')[0].innerText[2]"))*1000
                slot_machine = slot_machine + int(self.driver.execute_script("return document.getElementsByClassName('slotwrapper m-auto')[0].innerText[4]"))*100
                slot_machine = slot_machine + int(self.driver.execute_script("return document.getElementsByClassName('slotwrapper m-auto')[0].innerText[6]"))*10
                slot_machine = slot_machine + int(self.driver.execute_script("return document.getElementsByClassName('slotwrapper m-auto')[0].innerText[8]"))
                
            else:
                print('Only Cj can get VIP process')
        except:
            print("get_bonus_vip error")
        
        return slot_machine 
           
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
  
    sleep(2)
    resend_normal = 0
    try:
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        
        if time_in_minute > 355 or time_in_minute < 240:
            print('bot is doing there job right now!!!')
        else:
            print('Not in time')
            # exit()
            
        external_ip = "You know who am I"
        data_json = {'ip': external_ip , 'host' : 'jetsada'  ,'process' : 'get_user' }
        
        sleep(random.randint(0, 30)/100)
        data_get = json.loads(requests.post('http://128.199.236.187:8888/jesadabet/get_id',data=data_json ,timeout=120).text)
        # json_user = json.dumps(data.text)
        
        print(data_get)
        data = data_get['data']
        print(data)
        
        
        codename = str(list(data.keys())[0])
        time_delay = int(data[codename]['time_delay'])
        username = data[codename]['ID']
        bet_type = data[codename]['bet_type'] 
        normal_bet = int(data[codename]['normal'])
        
        if data[codename]['test'] == 'yes':
            test_process = True
        else:
            test_process = False
            

        if 1 == 1 :
            class_obj = yeekee_bot(data)

            a = subprocess.call("pkill chrome", shell=True)
            sleep(0.5)
            r = class_obj.create_connection()
                
                
            start = int(data[codename]['start'])
            end = int(data[codename]['end'])+1
            # sleep(2)
            
            get_af = int(data[codename]['get_af'])
            
            class_obj.room_number_normal , class_obj.state_normal = class_obj.get_room(user=codename,bet_type="normal",this_host=data[codename]['host'])
            class_obj.room_number_special , class_obj.state_special = class_obj.get_room(user=codename,bet_type=bet_type,this_host=data[codename]['host'])

            
            if get_af > 100 and data[codename]['host'] == 'thailotto':
                balance , point = class_obj.get_balance(codename)
                class_obj.get_af_thailotto(codename,balance)
                sleep(10) 
                class_obj.go_shoot_number(codename, int(data[codename]['time_delay']),test_process,bet_type,class_obj.room_number_special,class_obj.state_special)
                sleep(40)
              
            elif get_af > 100 and data[codename]['host'] == 'nakee':
                
                balance , point = class_obj.get_balance(codename)
                class_obj.get_af_nakee(codename,balance)
                sleep(10) 
                class_obj.go_shoot_number(codename, int(data[codename]['time_delay']),test_process,bet_type,class_obj.room_number_special,class_obj.state_special)
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
                
                if data[codename]['host'] == 'nakee' and bet_type == 'speed_double':
                    if start == 0:
                        for _n in range (5):
                            l.remove(_n*11)
                        for _n in range (50,55):
                            l.append(_n)
                    elif start == 50:
                        for _n in range (5):
                            l.remove((_n+5)*11)
                        for _n in range (45,50):
                            l.append(_n)
                                                
                
                if data[codename]['use_money'] == 'yes':
                    if (time_in_minute > 355 or time_in_minute < 240) and bet_type != 'normal':
                        now = datetime.datetime.now()
                        time_in_minute = (now.hour*60 + now.minute)
                        
                        
                        class_obj.select_number(codename,l,bet_type=bet_type,room=class_obj.room_number_special,state=class_obj.state_special)
                        
                        if now.minute in [13,14,15,16,28,29,30,31,43,44,45,46,58,59,0,1] and normal_bet == 1:
                            resend_normal = 1
                            class_obj.select_number(codename,l,bet_type="normal",room=class_obj.room_number_normal,state=class_obj.state_normal)
                            
                    elif (time_in_minute > 355 or time_in_minute < 240) and bet_type == 'normal':
            
                        class_obj.select_number(codename,l,bet_type=bet_type,room=class_obj.room_number_normal,state=class_obj.state_normal)
                        
                    else:
                        
                        class_obj.select_number(codename,l,bet_type=bet_type,room=class_obj.room_number_special,state=class_obj.state_special)
                
                
#################### เอาโบนัส ########################                
                try:
                    bonus_vip_num = class_obj.get_bonus_vip(codename,data[codename]['host'])
                except:
                    pass
                
                            
#################### ยิงเลข ########################
                if (time_in_minute > 355 or time_in_minute < 240) and bet_type != 'normal':
                    now = datetime.datetime.now()
                    time_in_minute = (now.hour*60 + now.minute)
                    
                    
                    class_obj.go_shoot_number(codename, int(data[codename]['time_delay']) ,test_process,bet_type,room=class_obj.room_number_special,state=class_obj.state_special,money=data[codename]['use_money'])
                    
                    sleep(3)
                    
                    if now.minute in [13,14,15,16,28,29,30,31,43,44,45,46,58,59,0,1] and normal_bet == 1:
                        resend_normal = 1
                        class_obj.go_shoot_number(codename, int(data[codename]['time_delay_normal']) ,test_process,bet_type="normal",room=class_obj.room_number_normal,state=class_obj.state_normal,money=data[codename]['use_money'])
                        
                     
                elif (time_in_minute > 355 or time_in_minute < 240) and bet_type == 'normal':
                    class_obj.go_shoot_number(codename, int(data[codename]['time_delay_normal']) ,test_process,bet_type="normal",room=class_obj.room_number_normal,state=class_obj.state_normal,money=data[codename]['use_money'])

                        
                else:
                    class_obj.go_shoot_number(codename, int(data[codename]['time_delay']),test_process,bet_type,room=class_obj.room_number_special,state=class_obj.state_special,money=data[codename]['use_money'])
                
                now = datetime.datetime.now()
                if now.minute in [2,17,32,47] :
                    pass
                else:        
                    sleep(10)
                    
                
                
                sleep(2)
            
            
            #### เช็ค balance ล่าสุด ####
            
            balance , point = class_obj.get_balance(codename)

            sleep(0.5)
            rank_normal = 0
            rank = 0
            print('balance  :' + str(balance) )
            sleep(0.5)



##################### get Rank ################################

            if get_af > 100:
                rank = 0
                number_shot = 99999
                bonus = 0

            else:
                if (time_in_minute > 355 or time_in_minute < 240) and bet_type != 'normal':
                    now = datetime.datetime.now()
                    time_in_minute = (now.hour*60 + now.minute)
                    
                    class_obj.rank_special = class_obj.get_result(codename,bet_type=bet_type)
                    print("class_obj.rank_special",class_obj.rank_special)
                    
                    if now.minute in [16,17,31,32,46,47,1,2] and normal_bet == 1:
                        class_obj.rank_normal = class_obj.get_result(codename,bet_type="normal")
                        print("class_obj.rank_normal",class_obj.rank_normal)
                        
                elif (time_in_minute > 355 or time_in_minute < 240) and bet_type == 'normal':
                    
                    class_obj.rank_normal = class_obj.get_result(codename,bet_type="normal")
                    print("class_obj.rank_normal",class_obj.rank_normal)
                    
                else:
                    class_obj.rank_special = class_obj.get_result(codename,bet_type=bet_type)
                    print("class_obj.rank_special",class_obj.rank_special)
                    
                    
                
                    
               
                # bonus = class_obj.bonus
                
                # last_rank_59 = class_obj.last_rank
                
            # sleep(0.5)
            # print('rank :' + str(rank))
            
            
            host = data[codename]['host'] 
            
            # room_number = int(class_obj.state) + 1
            
            # if movewinbet_twin == 1:
            #     room_number_normal = room_number
            #     room_number = (((room_number-1)*3)+(6*12))%288
            
            
            day_start_bet = (datetime.datetime.now() - datetime.timedelta(hours=5)).date()
            
            
######################## ส่งข้อมูลกลับ server #############################


            print('start send data')
            bonus = 0

            out = subprocess.check_output(["who", "-b"]).decode("utf-8")

            last_reboot = (str(out).split("\n")[0]).split(" ")
            date_format = '%Y-%m-%d %H:%M '
            date_str = ""

            for item in last_reboot:
                if item != "" and item != "boot" and item != "system":
                    date_str = date_str + item + " "
                
            date_obj = datetime.datetime.strptime(date_str, date_format) 
            print(date_obj)
            
            try:
                data_json_special = {'username' : username ,
                            'host' : data[codename]['host'] , 
                            'bet_type' : data[codename]['bet_type'] ,
                            'delay_use' : int(data[codename]['time_delay']) ,
                            'time_use' : class_obj.use_time_special,
                            'date' : day_start_bet , 
                            'use_money' : data[codename]['use_money'],
                            'bet_round' : class_obj.state_special+1 , 
                            'rank' : class_obj.rank_special , 
                            'last_rank' : class_obj.last_rank_special ,
                            'balance' : balance ,
                            'version' : version_yeekee ,
                            'bonus' : bonus ,
                            'number_shot' : class_obj.number_send_special ,
                            'get_af' : get_af ,
                            'point' : point , 
                            'last_reboot' : date_obj,
                            'server_delay' : data[codename]['server_delay'] ,
                            'bonus_vip_num' : bonus_vip_num
                            }
                print(data_json_special)
            except:
                pass
            
            if resend_normal == 1:
                delay_use = int(data[codename]['time_delay_normal'])
            else:
                delay_use = int(data[codename]['time_delay'])
            
            try:    
                data_json_normal = {'username' : username ,
                        'host' : data[codename]['host'] , 
                        'bet_type' : 'normal' ,
                        'delay_use' : delay_use ,
                        'time_use' : class_obj.use_time_normal,
                        'date' : day_start_bet , 
                        'use_money' : data[codename]['use_money'],
                        'bet_round' :  class_obj.state_normal+1, 
                        'rank' : class_obj.rank_normal , 
                        'last_rank' : class_obj.last_rank_normal ,
                        'balance' : balance ,
                        'version' : version_yeekee ,
                        'bonus' : bonus ,
                        'number_shot' : class_obj.number_send_normal ,
                        'get_af' : get_af ,
                        'point' : point , 
                        'last_reboot' : date_obj,
                        'server_delay' : data[codename]['server_delay'] ,
                        'bonus_vip_num' : bonus_vip_num
                        
                        }
                print(data_json_normal)
            except:
                pass
            
            now = datetime.datetime.now()
            print(now)
            # time_num = random.randint(0, 10)/10
            
            # if int(rank) == 0:
            #     time_num = time_num + 5
                
            # time.sleep(time_num)
            
            
            if (time_in_minute > 355 or time_in_minute < 240) and bet_type != 'normal':
                now = datetime.datetime.now()
                time_in_minute = (now.hour*60 + now.minute)
                
                r = requests.post('http://128.199.236.187:8888/jesadabet/send_history',data=data_json_special)
                print(r.status_code)
                sleep(1)
                if now.minute in [16,17,18,31,32,33,46,47,48,1,2,3] and normal_bet == 1:
                    r = requests.post('http://128.199.236.187:8888/jesadabet/send_history',data=data_json_normal)
                    print(r.status_code)
                
            elif (time_in_minute > 355 or time_in_minute < 240) and bet_type == 'normal':
                r = requests.post('http://128.199.236.187:8888/jesadabet/send_history',data=data_json_normal)
                print(r.status_code)
                
            else:
                r = requests.post('http://128.199.236.187:8888/jesadabet/send_history',data=data_json_special)
                print(r.status_code)
            
 
            
            
            class_obj.driver.quit()
            if data[codename]['host'] == 'nakee':
                class_obj.stop_display()
        
        
           
        
    except Exception as e :
        print(e)
        try:
            class_obj.driver.quit()
            if data[codename]['host'] == 'nakee':
                class_obj.stop_display()
        
        except:
            pass
        
        
    sleep(1)    
    a = subprocess.call("pkill chrome", shell=True)
    t = datetime.datetime.now()
    
   
    # class_obj.driver.quit()
    # class_obj.stop_display() 
    
    
    print('done')
    # sys.stdout.close()
    ################# add file ##################
    try:
        if data[codename]['host'] == "movewinbet" :
            today = datetime.datetime.now() + datetime.timedelta(minutes=3)
        else:
            today = datetime.datetime.now() - datetime.timedelta(hours=5)
            
        target_F = "/home/bitnami/project/xpsoft/log_data/"+ str(today.year) + "_" + str(today.month) + "_" + str(today.day)
        
        if not os.path.isdir("/home/bitnami/project/xpsoft/log_data"): 
            os.makedirs("/home/bitnami/project/xpsoft/log_data")   
               
        if not os.path.isdir(target_F): 
            os.makedirs(target_F)         
        
        if bet_type == "normal":        
            log_out = str(class_obj.state_normal+1)+".txt"     
        else:
            log_out = str(class_obj.state_special+1)+".txt"  
    except:
        pass

    sys.stdout.close()
    shutil.copyfile("/home/bitnami/project/xpsoft/outputfile.txt", target_F+"/"+log_out)
    sleep(1)
        
    sleep(1)
    exit()