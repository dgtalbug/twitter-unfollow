import tweepy
import time
from datetime import datetime
fix_date = datetime.strptime("2014-11-05 05:58:53", "%Y-%m-%d %H:%M:%S") # friends added after this date will be removed


auth = tweepy.OAuthHandler("xxxxxxxxxxxxxxxxx", 
                           "yyyyyyyyyyyyyyyyyyyyyyyyyyyyy") #consumer api key, consumer secret key 


auth.set_access_token("zzzzzzzzzzzzzzzzzzzzzzzzzzz",
                      "ssssssssssssssssssssssssssss")  # access token, access token secret

client = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
wait = 0

user = client.me()
print user.name

while True:
    try:
        for friend in tweepy.Cursor(client.friends).items():
            if friend.created_at > fix_date:
                print ">>>>>>>>>>>>>>>>>>>>>>>>"
                print friend.name
                print friend.created_at
                print "<<<<<<<<<<<<<<<<<<<<<<<<"
                client.destroy_friendship(friend.id)
                wait += 1
                if wait % 5 ==0:
                    print "waiting for 60sec"
                    time.sleep(60)
        break
    except tweepy.TweepError, e:
        print e
        continue
