
def get_room(code):
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


def post_number(code,room,num):
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

def get_balance(code):
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

def create_minigame(code):
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

def challenger_minigame(code,room):
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


def get_rank(code,room,page):
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