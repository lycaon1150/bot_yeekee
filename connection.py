import datetime
import multiprocessing
import pickle
import random
import re
import sched
import subprocess
import sys
import time
from typing import Tuple
import requests
import json

from multiprocessing import Process , Queue
from re import I
from threading import Thread
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import paramiter as setting

file_part = "/home/bitnami/project/xpsoft/bot/funtion/"

external_ip = requests.get('https://api.ipify.org').text
print(external_ip)



return_dict = Queue()


class yeekee_bot(object):
    def __init__(self, json_user):
        self.json_user = json_user
        self.session_data = {}
        print('success created')

    def create_connection(self):
        options = Options()
        options.add_argument('--headless')
        # Last I checked this was necessary.
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1920x1080')
    
    
        print('start create_connection')

        for user in self.json_user.keys():
            # set chorme user cookie
            # options.add_argument(
            #     "user-data-dir=%s%s" % (file_part , user))

            driver = webdriver.Chrome(
                ChromeDriverManager().install(), chrome_options=options)
            data_id = self.json_user[user]

            json_data = data_id

            

            json_data['driver'] = driver
            
            try:
                
                self.login(json_data['driver'], json_data['host'],json_data['ID'], json_data['Password'], json_data['url'])
           
            except:
                pass

            self.session_data[user] = json_data

    def login(self, driver, host, id, pwd, url):
        if host == 'jetsada' or host == 'huay':
            print(url)
            driver.get(url)
            
            sleep(1)
            if host == 'jetsada':
                driver.execute_script("document.getElementsByClassName('btn btn-bar btn-border btn-login-modal')[0].click();")
                sleep(1)
                
                
            driver.execute_script("document.getElementsByName('username')[0].value='%s';" % str(id))
            driver.execute_script("document.getElementsByName('password')[0].value='%s';" % str(pwd))
            sleep(1)
            driver.execute_script("document.querySelectorAll('button[type=submit]')[1].click();")
            print('done login')


    def jetsada_room(self):
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        if time_in_minute < 240:
            state = int((time_in_minute-347+1440)/15)
            
        else:
            state = int((time_in_minute-347)/15)
        
        return state

    def get_result_jetsada_bet(self,user,type):
        
        state = self.jetsada_room() - 1
        
        if type == 'special':
            start_number = 354  # strat the number of url
        elif type == 'normal':
            start_number = 172
            
        _url = str('https://www.jetsada.net/member/lottery/yeekee/%s' %(start_number+state))

        driver = self.session_data[user]['driver']
        driver.get(_url)
        
        sleep(3)
        
        print(_url)
        
        name = user.split("_")[1]
        print(name)
        secret_name = ""
        n = 0
        
        for c in name:
            if n == 3 or n == 4 or n == 5:
                secret_name = str(secret_name) + str('*')
            else:
                secret_name = str(secret_name) + str(c) 
            n = n + 1
        print(secret_name)
        for i in range(49):
            js = "return document.getElementsByClassName('username')[%s].innerText" %i
            find_name = driver.execute_script(js)
            # print(find_name)
            
            if find_name == name or find_name == secret_name:
                return i+1
        
        return 0
        
                
        

    def go_shoot_number(self, user, set_delay,test_setting,type):   # 225k no.16-25
        global return_dict
        this_host = self.session_data[user]['host']
        set_time_start = (21600 + 2*60) * 1000000
        time_par_round = 15*60*1000000
        server_delay = 0  # อันดับท้ายๆ เพิ่มค่า
        number_send = random.randint(10000, 99999)	
        if test_setting == True:
            test = time_par_round
        else:
            test = 0

        state = self.jetsada_room()
        if type == 'special':
            if this_host == 'jetsada':
                start_number = 354  # strat the number of url
            elif this_host == 'huay':
                start_number = 161
        elif type == 'normal':
            if this_host == 'jetsada':
                start_number = 172

        time_to_click = state*15+362
        hour = int(time_to_click/60)
        minute = int(time_to_click % 60)
        
        if state < 0:
            print('can not bet yet')
            return False
        else:
            print('start___BETTTT : %s' % str(this_host) )


        room = start_number+state
        
        # exceptions
        if type == 'normal' and this_host == 'jetsada':
            if room > 203:
                room = room + 5
                
                
                
        print(room)
        if this_host == 'jetsada':
            state_ref = 0
            _url = str('https://www.jetsada.net/member/lottery/yeekee/%s' % (room))
            if type == "special":
                js_send_number = 'axios.post("/member/lottery/yeekee", {number: "%s", bet_category_id: %s, yeekee_special: "plus"});' % (str(number_send),str(room))
            elif type == "normal":
                js_send_number = 'axios.post("/member/lottery/yeekee", {number: "%s", bet_category_id: %s, yeekee_special: ""});' % (str(number_send),str(room))
        
        elif this_host == 'huay':
            state_ref = 1
            _url = str('https://s1.huay.com/member#/lottery/yeekee/%s' % (room))
            js_send_number = 'axios.post("/protection/lottery/yeekee", { number: %s, bet_category_id: %s,main_type: 1}) ' % (str(number_send),str(room))
        
        driver = self.session_data[user]['driver']
        driver.get(_url)
    
      

        sleep(1)
        
        
        
        
        
        use_time = 0
        
        delay = (1000000-set_delay)/1000000
        while(1):
            now = datetime.datetime.now()
            time_in_microsec = (
                (now.hour*3600 + now.minute*60 + now.second)*1000000 + now.microsecond)
            loop_time = (time_in_microsec - set_time_start)
            
            
                
            if (loop_time - server_delay) % time_par_round > time_par_round - 1000000 - test and state_ref == 1:
                print('ckick 2st')
                sleep(delay)
                
                now = datetime.datetime.now()  
                driver.execute_script(js_send_number) 
                end = datetime.datetime.now()
                
                print('done : ' + str(user.split('_')[1]) + '\tnow : ' + str(now) + '\tuse time = ' + str(end-now) )
                use_time = (end-now).microseconds
                return_dict.put(use_time)
                break
            
            if state_ref == 0 :
                if (loop_time - server_delay) % time_par_round > time_par_round - 1000000*25 - test:
                    print('ckick 1st')
                    sleep(delay)
                    driver.refresh()
                    sleep(1.5)
                    driver.execute_script("document.getElementsByClassName('btn btn-secondary w-100')[0].click();")
                    sleep(0.5)
                    if type == "special" and this_host == "jetsada":
                        driver.execute_script("document.getElementsByClassName('btn btn-success w-100 btnYeekeeSubmit btn-shoot-plus')[0].click();") 
                    elif type == "normal" and this_host == "jetsada":
                        driver.execute_script("document.getElementsByClassName('btn btn-secondary w-100 btnYeekeeSubmit')[0].click();") 
     

                    # self.save_screenshots(user)
                    sleep(15.5)
                    driver.execute_script("document.getElementsByClassName('btn btn-secondary w-100')[0].click();")
                    sleep(0.5)
                    state_ref = 1
                
            
                
        sleep(0.1)
        # self.save_screenshots(user)

        print('end')
        
        


    def jetsada_select(self,user,list_number,type):
        state = self.jetsada_room()
        driver = self.session_data[user]['driver']

        if type == 'special':
            start_number = 354  # strat the number of url
        elif type == 'normal':
            start_number = 172


        if state < 0:
            print('can not bet yet')
            return False
        else:
            print('start___select')

            
        _url = str('https://www.jetsada.net/member/lottery/yeekee/%s' % (start_number+state))
        driver.get(_url)
        sleep(2)

        driver.execute_script("document.getElementsByClassName('link-tab')[1].click();")  
        sleep(1)

        driver.execute_script("document.getElementsByClassName('bet-list-item orange')[0].click();") 

        for n in list_number:
            bet_numer = n+1000
            driver.execute_script("document.getElementsByClassName('bet-items-square')[%s].click();" % bet_numer) 
            
        driver.execute_script("document.getElementsByClassName('btn btn-orange')[0].click();") 

        sleep(1)

        # driver.execute_script("return document.getElementsByClassName('input-bottom-bet float-left')[0];").send_keys(2)
        # sleep(1)
        driver.execute_script("document.getElementsByClassName('btn btn-primary btn-bet-l')[0].click();")
        sleep(1)
        driver.execute_script("document.getElementsByClassName('btn btn-primary btn-bet-l')[1].click();")
        sleep(1)
        
        # self.save_screenshots(user)
            

        
        pass

    def jesada_get_balance(self,user):
        # axios.get("/api/lottery-user-info/")
        driver = self.session_data[user]['driver']
        _url = 'https://www.jetsada.net/member/credit'

        driver.get(_url)
        sleep(1)
        balance = driver.execute_script("return document.getElementsByClassName('font-xxl')[0].innerText")
        
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
    
    sleep(random.randint(20,100)/10)
    
    try:
        now = datetime.datetime.now()
        time_in_minute = (now.hour*60 + now.minute)
        
        if time_in_minute > 355 or time_in_minute < 240:
            print('bot is doing there job right now!!!')
        else:
            print('Not in time')
            exit()
        
        data_json = {'ip': external_ip , 'host' : 'jetsada'  ,'process' : 'get_user' }
        
        data = json.loads(requests.post('http://128.199.236.187:8888/jesadabet/get_id',data=data_json).text)['data']
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
            

        if data[codename]['host'] == 'jetsada': 
            
            class_obj = yeekee_bot(data)
            
            class_obj.create_connection()

            start = int(data[codename]['start'])
            end = int(data[codename]['end'])+1
            sleep(2)
            
            l = [i for i in range(start,end)]
            if data[codename]['use_money'] == 'yes':
                class_obj.jetsada_select(codename,l,type=bet_type)

            thread = Process(target=class_obj.go_shoot_number,args=(codename, time_delay,test_process,bet_type))
            
            thread.start()
            thread.join()
            
            sleep(5)
            balance = class_obj.jesada_get_balance(codename)
            
            sleep(5)
            rank = class_obj.get_result_jetsada_bet(codename,bet_type)
            day_start_bet = (datetime.datetime.now() - datetime.timedelta(hours=5)).date()
            print('rank :' + str(rank))
            data_json = {'username' : username ,
                        'host' : data[codename]['host'] , 
                        'bet_type' : data[codename]['bet_type'] ,
                        'delay_use' : time_delay ,
                        'time_use' : return_dict.get(),
                        'date' : day_start_bet , 
                        'bet_round' : class_obj.jetsada_room() , 
                        'rank' : rank , 
                        'balance' : balance
                        }
            print(data_json)
            if class_obj.jetsada_room() < 89 or class_obj.jetsada_room() > 0:
                r = requests.post('http://128.199.236.187:8888/jesadabet/send_history',data=data_json)
                print(r.status_code)
                
                
                
                
    except Exception as e :
        print(e)
        
        
    sleep(2)
    a = subprocess.call("pkill chrome", shell=True)

    sleep(2)
    exit()

