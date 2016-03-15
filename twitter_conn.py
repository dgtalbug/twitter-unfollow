import tweepy
import time
from datetime import datetime
fix_date = datetime.strptime("2014-11-05 05:58:53", "%Y-%m-%d %H:%M:%S")


auth = tweepy.OAuthHandler("xxxxxxxx",
                           "yyyyyyyyyy")


auth.set_access_token("000000000-zzzzzzzzzzzzzz",
                      "dfadasssssssssssssss")

client = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
wait = 0

user = client.me()
print user.name

while True:
    try:
        for friend in tweepy.Cursor(client.friends).items(2942):
            if friend.created_at > fix_date:
                print "reaching"
                print friend.name
                print friend.created_at
                client.destroy_friendship(friend.id)
                wait += 1
                if wait % 5 ==0:
                    print "waiting"
                    time.sleep(60)
        break
    except tweepy.TweepError, e:
        print e
        continue
