import tweepy
import time
from datetime import datetime
fix_date = datetime.strptime("2014-11-05 05:58:53", "%Y-%m-%d %H:%M:%S")


auth = tweepy.OAuthHandler("p34sYvWiq22v7fQPiv8FjlU8r",
                           "aYHbQOcO7q8m1sKv6ACGY078K1DBob6onvIlKElMIkdYSf4MCg")

auth.set_access_token("317918338-oOHo9Y1AZ2HJWYNnCZ89N7lszbZxVv1M0n77FOcE",
                      "ztKIEukoEaxk2ezrc5pb5aUUmWg13bqE8F9kQ9asfUu32")

client = tweepy.API(auth, wait_on_rate_limit=True)
wait = 0

user = client.me()
print user.name

friends = client.friends()
while True:
    try:
        for friend in tweepy.Cursor(client.friends).items():
            if friend.created_at > fix_date:
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