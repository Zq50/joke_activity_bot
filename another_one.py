import urllib3
import json

urls = json.load(open("source/url.json"))
poll = urllib3.PoolManager()
def joke():
    resp = poll.request('GET',urls['randJokeApi'])
    data = resp.data
    joke= json.loads(data)  
    ret= joke['setup'] + " " + joke['punchline']
    return ret

def bored():
    resp = poll.request('GET',urls['boredApi'])
    activity = json.loads(resp.data) 
    return activity['activity']