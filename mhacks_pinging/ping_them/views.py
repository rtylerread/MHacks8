from django.shortcuts import render
from django.http import HttpResponse
import random as rand
import oauth2
import json
from .models import url_to_ping

# Create your views here.

def oauth_req(url, http_method, post_body="", http_headers=None):
    my_oauth_token = '784670637918920704-WTwOBKMVS0RTCYV5N8zinHlhyOYcqE7'
    my_oauth_secret = 'oecKOyweOgI78mSQVvW0EbJrOzmyfKONhRIztSeqWeuPM'
    consumer_key = 'dB85X93dkTOturiWdPdbMoWxx'
    consumer_secret = 'NqivUy4vKJKAMjODrk1Q41sTXUmgdUsY2fKkx33EaMTLbdJ7zO'
    #the above is realllly bad style. absolute disregard for secutity.
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    client = oauth2.Client(consumer,oauth2.Token(my_oauth_token, my_oauth_secret))
    respond,content = client.request(url, http_method, post_body, http_headers)
    return content


def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0

def tweet_them(twitter_id, first_time, url):
    tweet_text = twitter_id
    if(first_time):
        tweet_text = 'Hello! We are contacting you to let you know that one of your student resources has become unavailable. Testing: ' + url       
    else:
        choose = rand.randint(0,10)
        if choose == 0:
            tweet_text += 'Servers are still down! We think you should either replace your IT staff or burn your servers. Testing: ' + url
        elif choose == 1:
            tweet_text += 'An SQL statement walks into a bar and sees two tables. It approaches, and asks \"may I join you?\"  Also, your servers are down. Testing: ' + url
        elif choose == 2:
            tweet_text += 'We know you guys are super busy with password resets but just FYI, your servers are still down. Testing: ' + url
        elif choose == 3:
            tweet_text += 'test 3'
        elif choose == 4:
            tweet_text += 'test 4'
        elif choose == 5:
            tweet_text += 'test 5'
        elif choose == 6:
            tweet_text += 'test 6'
        elif choose == 7:
            tweet_text += 'test 7'
        elif choose == 9:
            tweet_text += 'test 8'
        elif choose == 10:
            tweet_text += 'test 9'
        tweet_this = "status="+tweet_text+"&&lat=41.8797907&&long=-87.6307392&&display_coordinates=true"
        timeline = json.loads(oauth_req('https://api.twitter.com/1.1/statuses/update.json','POST',tweet_this))

    if 'errors' in timeline:
        print("Error received from Twitter API. Error code(s): ")
        for k in range(len(timeline['errors'])):
            print(timeline['errors'][k]['code'])
        
def check_all():
    for i in range(1,url_to_ping.objects.all().count()):
        print i
        current = url_to_ping.objects.get(id=i)
        if not ping(current.url):
            tweet_them(current.twitter_id, 
                       current.first_time, 
                       current.url)
        else:
            print 'Ping Successful for: ' + current.twitter_id
