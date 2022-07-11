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



def post_number_jesadabet(code,room,num):
    js = """fetch('https://thailotto.com/member/lottery/yeekee', {
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