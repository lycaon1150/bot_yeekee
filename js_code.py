def login_nakee(username,password):
    js = """return await fetch('https://nakee.com/auth/login', {
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



def get_room_nakee(code):
    js = """return await fetch('https://nakee.com/api/member/lotto', {
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



def post_number_nakee(code,room,num):
    js = """fetch('https://nakee.com/api/member/lotto/shoot/number/%s', {
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


def bet_number_nakee(code,link,bet_text):
    js = """fetch('https://nakee.com/api/game/lotto/%s', {
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

def get_balance_nakee(code):
    js = """return await fetch('https://nakee.com/auth/me', {
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

def create_minigame_nakee(code):
    js = """fetch('https://nakee.com/api/game/minigame/lucky/paoyingchub/creator', {
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

def challenger_minigame_nakee(code,room):
    js = """fetch('https://nakee.com/api/game/minigame/lucky/paoyingchub/challenger', {
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


def get_rank_nakee(code,room,page):
    js = """return await fetch('https://nakee.com/api/member/lotto/shoot/number/%s?page=%s', {
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

def get_bonus_nakee(code,room):
    js = """return await fetch('https://nakee.com/api/member/lotto/shoot/number/%s?uniqueId=rand_3', {
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

def bet_number_movewinbet(room,betList,bet_url):
    


    js = """
    
    function getMeta(metaName) {
    const metas = document.getElementsByTagName('meta');

    for (let i = 0; i < metas.length; i++) {
        if (metas[i].getAttribute('name') === metaName) {
        return metas[i].getAttribute('content');
        }
    }

    return '';
    }
            
    var code = getMeta('csrf-token')
    
    
    var myHeaders = new Headers();
    myHeaders.append("x-csrf-token", code);


    var formdata = new FormData();
    formdata.append("bet_category_id", '%s');
    formdata.append("categoryGroup", 'lotto');
    formdata.append("betListJsonStringify", '%s');

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: formdata,
    redirect: 'follow'
    };

    fetch( '%s' , requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));""" % (str(room),str(betList) , str(bet_url))
    
    return js

def post_multitime_number_movewinbet(room,num,domain_name,type_bet):
    
    if type_bet == 'normal':
        type_url = 'yeekee'
    else:
        type_url = 'yeekee-vip'


    js = """
    
    function getMeta(metaName) {
    const metas = document.getElementsByTagName('meta');

    for (let i = 0; i < metas.length; i++) {
        if (metas[i].getAttribute('name') === metaName) {
        return metas[i].getAttribute('content');
        }
    }

    return '';
    }
            
    var code = getMeta('csrf-token')
    
    
    var myHeaders = new Headers();
    myHeaders.append("x-csrf-token", code);


    var formdata = new FormData();
    formdata.append("number", "%s");

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: formdata,
    redirect: 'follow'
    };
    for (let i = 0; i < 10; i++) {
        fetch("https://%s/member/%s/%s/bet-number", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error)); }""" % (str(num),str(domain_name),str(type_url),str(room))
    
    return js


def post_number_movewinbet(room,num,domain_name,type_bet):
    
    if type_bet == 'normal':
        type_url = 'yeekee'
    else:
        type_url = 'yeekee-vip'


    js = """
    
    function getMeta(metaName) {
    const metas = document.getElementsByTagName('meta');

    for (let i = 0; i < metas.length; i++) {
        if (metas[i].getAttribute('name') === metaName) {
        return metas[i].getAttribute('content');
        }
    }

    return '';
    }
            
    var code = getMeta('csrf-token')
    
    
    var myHeaders = new Headers();
    myHeaders.append("x-csrf-token", code);


    var formdata = new FormData();
    formdata.append("number", "%s");

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: formdata,
    redirect: 'follow'
    };

    fetch("https://%s/member/%s/%s/bet-number", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));""" % (str(num),str(domain_name),str(type_url),str(room))
    
    return js

def post_multitime_thailotto(code,room,num):
    js = """
        
        function getCookie(name) {
                    const value = `; ${document.cookie}`;
                    const parts = value.split(`; ${name}=`);
                    if (parts.length === 2) return parts.pop().split(';').shift();
                    }
                
        var code = getCookie('XSRF-TOKEN')
        
        for (let i = 0; i < 5; i++) {

            fetch('https://lotto5555.com/member/lottery/yeekee', {
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
    })}""" % (str(code),str(num),str(room))
    return js

def post_number_jesadabet(code,room,num):
    js = """
    
    async function getCookie(name) {
                const value = `; ${document.cookie}`;
                const parts = value.split(`; ${name}=`);
                if (parts.length === 2) return parts.pop().split(';').shift();
                }
            
    var code = await getCookie('XSRF-TOKEN')
    
    
    return await fetch('https://lotto5555.com/member/lottery/yeekee', {
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
}).then(response => { return response.json() } );""" % (str(code),str(num),str(room))
    return js



def bet_number_jesadabet(code,bet_text):
    js = """fetch('https://lotto5555.com/member/lottery', {
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


def post_bonus_thailotto():
    js = """function getCookie(name) {
                const value = `; ${document.cookie}`;
                const parts = value.split(`; ${name}=`);
                if (parts.length === 2) return parts.pop().split(';').shift();
                }
            
        var code = getCookie('XSRF-TOKEN')
        
        
        fetch('https://lotto5555.com/member/game/lucky-box', {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json' ,
            'x-xsrf-token': code
        }
        
    })""" 
    
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

def get_vip_nakee(code,vip):
    js = """ await fetch('https://nakee.com/api/member/privilege/bonus', {
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


def check_vip_nakee(code):
    js = """ return await fetch('https://nakee.com/api/member/privilege/bonus', {
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