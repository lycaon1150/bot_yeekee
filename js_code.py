def login_chudjenbet(username,password):
    js = """return await fetch('https://chudjenbet.com/auth/login', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
    },
    'body': JSON.stringify({"username":"%s","password":"%s"})
    }).then(response => { return response.json() } ); """ % (str(username),str(password))

    return js



def get_room_chudjenbet(code):
    js = """return await fetch('https://chudjenbet.com/api/member/lotto', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'authorization': '%s'
        }
    }).then(response => { return response.json() } );""" % str(code)
    
    return js

def get_room_ltobet(tpye,code):
    js = """return await fetch('https://www.ltobet.com/api/member/lotto?type=%s', { 
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'authorization': '%s'
        }
    }).then(response => { return response.json() } );""" % (str(tpye),str(code))
    
    return js



def post_number_chudjenbet(code,room,num):
    js = """fetch('https://chudjenbet.com/api/member/lotto/shoot/number/%s', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
            ,
        'authorization': '%s'
    },
    'body': JSON.stringify({
        "number": "%s"
    })
})""" % (str(room),str(code),str(num))

    return js


def post_number_ltobet(code,room,num,bet_type):
    
    if bet_type == 'zodiac':
        url_api = 'https://www.ltobet.com/api/member/lotto/shoot/zodiac_number/%s' % room
    else:
        url_api = 'https://www.ltobet.com/api/member/lotto/shoot/number/%s' % room
        
    js = """fetch('%s', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
            ,
        'authorization': '%s'
    },
    'body': JSON.stringify({
        "number": "%s"
    })
})""" % (str(url_api),str(code),str(num))

    return js


def bet_number_chudjenbet(code,link,bet_text):
    js = """fetch('https://chudjenbet.com/api/game/lotto/%s', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
            ,
        'authorization': '%s'
    },
    'body': JSON.stringify(%s)
})""" % (str(link),str(code),str(bet_text))
   
    return js

def bet_number_ltobet(code,link,bet_text):
    
    if link == 'zodiac':
        url_api = 'https://www.ltobet.com/api/game/lotto_zodiac/zodiac'
    else:
        url_api = 'https://www.ltobet.com/api/game/lotto/%s' % link
    
    js = """fetch('%s', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
            ,
        'authorization': '%s'
    },
    'body': JSON.stringify(%s)
})""" % (str(url_api),str(code),str(bet_text))
   
    return js

def get_balance_chudjenbet(code):
    js = """return await fetch('https://chudjenbet.com/auth/me', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'authorization': '%s'
        }
    }).then(response => { return response.json() } );""" % str(code)
    
    return js

def get_balance_ltobet(code):
    js = """return await fetch('https://www.ltobet.com/auth/me', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'authorization': '%s'
        }
    }).then(response => { return response.json() } );""" % str(code)
    
    return js

def create_minigame_chudjenbet(code):
    js = """fetch('https://chudjenbet.com/api/game/minigame/lucky/paoyingchub/creator', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
            ,
        'authorization': '%s'
    },
    'body': JSON.stringify({"choice" : "PAPER", "amount" : "50"})
})""" % (str(code))
    return js

def challenger_minigame_chudjenbet(code,room):
    js = """fetch('https://chudjenbet.com/api/game/minigame/lucky/paoyingchub/challenger', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
            ,
        'authorization': '%s'
    },
    'body': JSON.stringify({ "choice" : "HAMMER", "creator_id" : "%s"})
})""" % (str(code),str(room))
    return js


def get_rank_chudjenbet(code,room,page):
    js = """return await fetch('https://chudjenbet.com/api/member/lotto/shoot/number/%s?page=%s', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'authorization': '%s'
        }
    }).then(response => { return response.json() } );""" % (str(room),str(page),str(code))
    
    return js

def get_bonus_chudjenbet(code,room):
    js = """return await fetch('https://chudjenbet.com/api/member/lotto/shoot/number/%s?uniqueId=rand_3', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'authorization': '%s'
        }
    }).then(response => { return response.json() } );""" % (str(room),str(code))
    
    return js

def get_rank_ltobet(code,room,page,bet_type):
    
    if bet_type == 'zodiac':
        url_room = 'https://www.ltobet.com/api/member/lotto/shoot/zodiac_number/%s?page=%s' % (str(room),str(page))
    else:
        url_room = 'https://www.ltobet.com/api/member/lotto/shoot/number/%s?page=%s' % (str(room),str(page))
    
    js = """return await fetch('%s', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'authorization': '%s'
        }
    }).then(response => { return response.json() } );""" % (url_room,str(code))
    
    return js

def post_number_jesadabet(code,room,num):
    js = """
    
    function getCookie(name) {
                const value = `; ${document.cookie}`;
                const parts = value.split(`; ${name}=`);
                if (parts.length === 2) return parts.pop().split(';').shift();
                }
            
    var code = getCookie('XSRF-TOKEN')
    
    
    fetch('https://thailotto.com/member/lottery/yeekee', {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded', 
            ,
            // 'x-xsrf-token': '%s'
        
        'x-xsrf-token': code
    },
    'body': JSON.stringify({
        "number":"%s","bet_category_id":%s,"yeekee_special":""
    })
})""" % (str(code),str(num),str(room))
    return js



def bet_number_jesadabet(code,bet_text):
    js = """fetch('https://thailotto.com/member/lottery', {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                    'Content-Type': 'application/json'
                        // 'Content-Type': 'application/x-www-form-urlencoded', 
                        ,
                    'x-xsrf-token': '%s'
                },
                'body': JSON.stringify(%s)
                })""" % (str(code),str(bet_text))
    return js


def post_bonus_jesadabet(code):
    js = """fetch('https://thailotto.com/member/game/lucky-box', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded', 
                ,
            'x-xsrf-token': '%s'
        }
            })""" % (str(code))
    
    return js

def post_number_ruay(room,number,url):
    js = """var data = "ynum%5Bid%5D=""" + str(room) + """&ynum%5Bying%5D=""" + str(number) + """";

            var xhr = new XMLHttpRequest();
            xhr.withCredentials = true;

            xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                console.log(this.responseText);
            }
            });

          
            
            """ + """xhr.open("POST", "%s",true);""" % (url) + """
            xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
            xhr.setRequestHeader("cache-control", "no-cache");
            xhr.send(data);
            """
            
    return js

def get_vip_ltobet(code,vip):
    js = """ await fetch('https://www.ltobet.com/api/member/privilege/bonus', {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json'
                    // 'Content-Type': 'application/x-www-form-urlencoded', 
                    ,
                'authorization': '%s'
            },
            'body': JSON.stringify({"vip" : "%s"})
        }).then(response => { return response.json() } ); """ % (str(code),str(vip))
    
    
    
    return js


def check_vip_ltobet(code):
    js = """ return await fetch('https://www.ltobet.com/api/member/privilege/bonus', {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json',
                'authorization': '%s'
                    // 'Content-Type': 'application/x-www-form-urlencoded', 
            }
            }).then(response => { return response.json() } ); """ % (str(code))
    
    
    
    return js

def get_vip_chudjenbet(code,vip):
    js = """ await fetch('https://chudjenbet.com/api/member/privilege/bonus', {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json'
                    // 'Content-Type': 'application/x-www-form-urlencoded', 
                    ,
                'authorization': '%s'
            },
            'body': JSON.stringify({"vip" : "%s"})
        }).then(response => { return response.json() } ); """ % (str(code),str(vip))
    
    
    
    return js


def check_vip_chudjenbet(code):
    js = """ return await fetch('https://chudjenbet.com/api/member/privilege/bonus', {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
                'Content-Type': 'application/json',
                'authorization': '%s'
                    // 'Content-Type': 'application/x-www-form-urlencoded', 
            }
            }).then(response => { return response.json() } ); """ % (str(code))
    
    
    
    return js