import code
from curses import reset_shell_mode
import datetime
from lib2to3.pgen2 import driver
import multiprocessing
import pickle
import random
import re
import sched
import subprocess
import sys
import time
from typing import Tuple
from webbrowser import get
import requests
import json

from multiprocessing import Process , Queue
from re import I
from threading import Thread
from time import sleep

import selenium
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc


import js_code

import paramiter as setting

file_part = "/home/bitnami/project/xpsoft/bot/funtion/"

external_ip = requests.get('https://api.ipify.org').text
print(external_ip)



return_dict = Queue()


class yeekee_bot(object):
    def __init__(self, json_user):
        self.json_user = json_user
        self.session_data = {}
        self.room_url = ""
        self.room_number = ""
        self.state = ""
        print('success created')

    def create_connection(self):
        
        PROXY = "Selnyolycaon:F7k1KtH@154.16.11.95:45785"
        
        

        print('start create_connection')

        for user in self.json_user.keys():
            
            
            # if self.json_user[user]['host'] == "jetsada" or self.json_user[user]['host'] == "thailotto":
            #     options = Options()
            #     # options.add_argument('--proxy-server=203.150.128.60:8080')
            #     options.add_argument('--headless')
            #     # Last I checked this was necessary.
            #     options.add_argument('--disable-gpu')
            #     options.add_argument('window-size=1920x1080')
            #     # options.add_argument('sec-ch-ua-platform=Windows')
            #     # options_seleniumWire = {
            #     #     'proxy': {
            #     #         # 'https': 'https://Selnyolycaon:B2p3GpX@154.16.11.95:45785'
            #     #         # 'http : http://203.150.128.60:8080'
            #     #     }
            #     # }
        
            # elif self.json_user[user]['host'] == 'chudjenbet':
            options = uc.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument('window-size=1920x1080')
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
            # set chorme user cookie
            # options.add_argument(
            #     "user-data-dir=%s%s" % (file_part , user))

            # if self.json_user[user]['host'] == "jetsada" or self.json_user[user]['host'] == "thailotto":
            #     driver = webdriver.Chrome(
            #         ChromeDriverManager().install(), chrome_options=options ,
            #         # seleniumwire_options=options_seleniumWire
            #         )
                
            # elif self.json_user[user]['host'] == 'chudjenbet':
                
            driver = uc.Chrome(version_main=93, options=options)    
            
            
            data_id = self.json_user[user]

            json_data = data_id
            
            driver.get('https://api.ipify.org')
            sleep(1)
            driver.save_screenshot('ip.png')
            json_data['driver'] = driver
            json_data['authorization']  = ''
            
            try:
                
                self.login(json_data['driver'], json_data['host'],json_data['ID'], json_data['Password'], json_data['url'])
                if self.json_user[user]['host'] == 'chudjenbet':
                    json_data['authorization'] = driver.execute_script("return window.localStorage['auth._token.local']")                
                elif self.json_user[user]['host'] == 'thailotto':
                    json_data['authorization'] = driver.execute_script("return (await window.cookieStore.get('XSRF-TOKEN')).value")  
            except:
                pass

            self.session_data[user] = json_data

    def login(self, driver, host, id, pwd, url):
        print(url)
        driver.get(url)
        sleep(5)
        print(driver.execute_script('return navigator.webdriver'))
        if host == 'jetsada' or host == 'huay' or host == 'thailotto':
            
            if host == 'jetsada':
                driver.execute_script("document.getElementsByClassName('btn btn-bar btn-border btn-login-modal')[0].click();")
                class_username = 'username'
                sleep(1)
            elif host == 'thailotto':
                driver.execute_script("document.getElementsByClassName('btn btn-bar btn-login-modal')[0].click();")
                sleep(1)
                
            
            driver.execute_script("document.getElementsByName('username')[0].value='%s';" % str(id))
            driver.execute_script("document.getElementsByName('password')[0].value='%s';" % str(pwd))
            sleep(1)
            driver.execute_script("document.querySelectorAll('button[type=submit]')[1].click();")
            print('done login')
        elif host == 'chudjenbet':
            
            try:
                print(driver.execute_script("return document.querySelectorAll('button[type=submit]')[0].disabled = false;"))
                sleep(2)
                driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys(str(id))
                driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(str(pwd))
                # print(driver.execute_script("return document.getElementsByClassName('app__form-control bg-white')[0].value='%s';" % str(id)))
                # print(driver.execute_script("return document.getElementsByClassName('app__form-control bg-white')[1].value='%s';" % str(pwd)))
                sleep(2)
                driver.execute_script("return document.querySelectorAll('button[type=submit]')[0].click();")
                sleep(2)
            except:
                pass
            print('done login')
        
        driver.save_screenshot('login.png')
        
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
    
    

    def get_result(self,user,bet_type):
        print('do process get_result')
        print('get rank')
        print(self.room_url)
        print(self.room_number)
        # _url = str('https://www.jetsada.net/member/lottery/yeekee/%s' %(start_number+state))

        driver = self.session_data[user]['driver']
        driver.get(self.room_url)
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        sleep(3)
        
        # print(self.room_url)
        
        name = user.split("_")[1]
        print(name)
        secret_name = ""
        
        if this_host == 'jetsada' or this_host == 'thailotto':
            n = 0
            for c in name:
                if n == 3 or n == 4 or n == 5:
                    secret_name = str(secret_name) + str('*')
                else:
                    secret_name = str(secret_name) + str(c) 
                n = n + 1
            print(secret_name)
        
        
            for i in range(50):
                js = "return document.getElementsByClassName('username')[%s].innerText" %i
                find_name = driver.execute_script(js)
                # print(find_name)
                
                if find_name == name or find_name == secret_name:
                    return i+1
                
                
        elif this_host == 'chudjenbet':
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
           
            result = []
            for i in range(1,4):
                _r = list(driver.execute_script(str(js_code.get_rank_chudjenbet(code,room,i)))['records'])
                # print(_r)
            
                for data in _r:
                
                    result.append(data['username'])

           
            for rank , username in enumerate(result):
              
                if str(secret_name) == str(username):
                    return rank+1
        
        print('end process get_result')
        return 0
        
    def get_room(self,user):
        
        this_host = self.session_data[user]['host']
        driver = self.session_data[user]['driver']
        code = self.session_data[user]['authorization']
        bet_type = self.session_data[user]['bet_type']
        if this_host == 'jetsada':
            state = self.room_88()
            if bet_type == 'special':
                start_number = 354  # strat the number of url
            elif bet_type == 'normal':
                start_number = 172

        elif this_host == 'huay':
            if bet_type == 'normal':
                state = self.room_264()
                start_number = 514
        
        elif this_host == 'thailotto':
            if bet_type == 'special':
                start_number = 450  
                state = self.room_264()
                
            elif bet_type == 'normal':
                start_number = 172
                state = self.room_88()
                
        elif this_host == 'chudjenbet':
            data_room_chudjenbet = driver.execute_script(js_code.get_room_chudjenbet(code))

            if bet_type == 'special':
                for item in data_room_chudjenbet['records']:
                    if item['category_id'] == 1401:
                        start_number = int(item['id'])
                        break
                state = self.room_264()

            elif bet_type == 'vip_264':
                for item in data_room_chudjenbet['records']:
                    if item['category_id'] == 1701:
                        start_number = int(item['id'])
                        break
                state = self.room_264()
                
            elif bet_type == 'normal':
                for item in data_room_chudjenbet['records']:
                    if item['category_id'] == 101:
                        start_number = int(item['id'])
                        break
                
                state = self.room_88()
            
            
        room = start_number+state       
        # exceptions
        if this_host == 'jetsada' or this_host == 'thailotto':
            if bet_type == 'normal':
                if room > 203:
                    room = room + 5

        
        return room , state
    
    
    def go_shoot_number(self, user, set_delay,test_setting,bet_type):   # 225k no.16-25
        global return_dict
        code = self.session_data[user]['authorization']
        this_host = self.session_data[user]['host']
        set_time_start = (21600 + 2*60) * 1000000
        
        server_delay = 0  # อันดับท้ายๆ เพิ่มค่า
        number_send = random.randint(10000, 99999)	
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
                
        elif this_host == 'chudjenbet':
            if bet_type == 'special' or bet_type == 'vip_264' :
                time_to_click = state*5+361
                set_time_start = (21600 + 1*60) * 1000000
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
            _url = str('https://thailotto.com/member/lottery/yeekee/%s' % (room))
            
            # js_send_number = 'axios.post("/member/lottery/yeekee", {number: "%s", bet_category_id: %s, yeekee_special: ""});' % (str(number_send),str(room))
            js_send_number = str(js_code.post_number_jesadabet(code,room,number_send))
        elif this_host == 'chudjenbet':
            state_ref = 0
            _url = str('https://chudjenbet.com/member/lotto/%s' % (room))
            js_send_number = str(js_code.post_number_chudjenbet(code,room,number_send))
            
        driver = self.session_data[user]['driver']
        # driver.get(_url)
        sleep(2)
        driver.save_screenshot('shot.png')
        self.room_url = _url
        self.room_number = room
        self.state = state
        sleep(1)
        
        
        
        
        
        use_time = 0
        rand_time = (25 + random.randint(0, 4))

        delay = (1000000-set_delay)/1000000
        while(1):
            now = datetime.datetime.now()
            time_in_microsec = (
                (now.hour*3600 + now.minute*60 + now.second)*1000000 + now.microsecond)
            loop_time = (time_in_microsec - set_time_start)
            
            
                
            if (loop_time - server_delay) % time_par_round > time_par_round - 1000000 - test and state_ref == 1:
                print('ckick to win')
                sleep(delay)
    
                now = datetime.datetime.now()  
                driver.execute_script(js_send_number) 
                end = datetime.datetime.now()
                
                print('done : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now) )
                use_time = (end-now).microseconds
                return_dict.put(use_time)
                break
            

            if state_ref == 0 :
                if (loop_time - server_delay) % time_par_round > time_par_round - 1000000*rand_time - test:
                    print('ckick 1st')
                    sleep(delay)
                    driver.refresh()
                    sleep(1.5)
                    driver.save_screenshot('1150.png')
                          
                    sleep(0.5)
                    
                    ######### ยิงเลขครั้งแรก ##############
                    
                    driver.execute_script(js_send_number) 
           
                    sleep(15.5)
                
                   
                    state_ref = 1
                
            
                
        sleep(0.1)
        # self.save_screenshots(user)

        print('end process shot number')
        
        
        


    def select_number(self,user,list_number,bet_type):
        
        driver = self.session_data[user]['driver']
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        
        room , state = self.get_room(user)

        ###### set url for go shot number #########
            
        if state < 0:
            print('can not bet yet')
            return False
        else:
            print('start___select')
 
        # driver.get(_url)
        sleep(2)


        if this_host == 'jetsada' or this_host == 'thailotto':
            betListJsonStringify = '['
    
            for n in list_number:
                if n < 10:
                    n = str(0) + str(n)
                
                betListJsonStringify = betListJsonStringify + str(r'{\"type\":3,\"slug\":\"bet_two_top\",\"number\":\"%s\",\"price\":%s},' % (str(n),str(2)))
            
            count_n = len(betListJsonStringify)
            betListJsonStringify = list(betListJsonStringify)
            betListJsonStringify[count_n-1] = ']'
            betListJsonStringify = ''.join(betListJsonStringify)

            bet_text = '{"stake_method":2,"bet_category_id":%s,"betListJsonStringify":"%s","thaistock20checklist":[]}' % (str(room),betListJsonStringify)
           
            js = js_code.bet_number_jesadabet(code,bet_text)

            driver.execute_script(js)
        
        print('done bet number')


    def get_balance(self,user):
        
        print('do process get_balance')
        
        driver = self.session_data[user]['driver']
        this_host = self.session_data[user]['host']
        code = self.session_data[user]['authorization']
        
        if this_host == 'thailotto' or this_host == 'jetsada':
            _url = self.session_data[user]['url_balance'] + str(self.session_data[user]['ID'])
            driver.get(_url)
            sleep(1)
            # driver.save_screenshot('11111.png')

            balance = driver.execute_script("return document.body.innerText")
        
        elif this_host == 'chudjenbet':
            balance = driver.execute_script(str(js_code.get_balance_chudjenbet(code)))['data']['real_credit']
        
        
        return balance

        

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
    
    # sleep(random.randint(0,150)/10)
    
    try:
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        
        if time_in_minute > 355 or time_in_minute < 240:
            print('bot is doing there job right now!!!')
        else:
            print('Not in time')
            exit()
        
        data_json = {'ip': external_ip , 'host' : 'jetsada'  ,'process' : 'get_user' }
        
        data = json.loads(requests.post('http://128.199.236.187:8888/jesadabet/get_id',data=data_json ,timeout=60).text)['data']
        # json_user = json.dumps(data.text)
        print(data)
        
        
        codename = str(list(data.keys())[0])
        time_delay = int(data[codename]['time_delay'])
        username = data[codename]['ID']
        
        bet_type = data[codename]['bet_type'] 
   
        
        if data[codename]['test'] == 'yes':
            test_process = True
        else:
            test_process = False
            

        if data[codename]['host'] == 'jetsada' or data[codename]['host'] == 'thailotto' or data[codename]['host'] == 'chudjenbet' : 
            
            class_obj = yeekee_bot(data)
            
            class_obj.create_connection()

            start = int(data[codename]['start'])
            end = int(data[codename]['end'])+1
            sleep(2)
            
            l = [i for i in range(start,end)]
            if data[codename]['use_money'] == 'yes':
                class_obj.select_number(codename,l,bet_type=bet_type)


            #### ยิงเลข ####
            class_obj.go_shoot_number(codename, time_delay,test_process,bet_type)
            sleep(5)
            
            #### เช็ค balance ล่าสุด ####
            balance = class_obj.get_balance(codename)
            
            print('balance  :' + str(balance) )
            sleep(5)
            rank = class_obj.get_result(codename,bet_type)
            print('rank :' + str(rank))
            
            
            host = data[codename]['host'] 
            room_number = class_obj.state + 1
            
            day_start_bet = (datetime.datetime.now() - datetime.timedelta(hours=5)).date()
            
            
            data_json = {'username' : username ,
                        'host' : data[codename]['host'] , 
                        'bet_type' : data[codename]['bet_type'] ,
                        'delay_use' : time_delay ,
                        'time_use' : return_dict.get(),
                        'date' : day_start_bet , 
                        'bet_round' : room_number , 
                        'rank' : rank , 
                        'balance' : balance
                        }
            print(data_json)
        
            r = requests.post('http://128.199.236.187:8888/jesadabet/send_history',data=data_json)
            print(r.status_code)
                
                
                
                
    except Exception as e :
        print(e)
        
        
    sleep(2)    
    a = subprocess.call("pkill chrome", shell=True)

    sleep(2)
    exit()

