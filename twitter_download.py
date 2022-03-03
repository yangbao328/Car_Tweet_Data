"""
DS3500 HW2
Tianyang Bao, John Drohan, Amaris Han 
"""

import re
import csv
import tweepy
import time

# Ask user for carmaker they'd like to analyze
carmaker = input('What are the brands you want to include?').upper().split()
#['AUDI','BMW','MERCEDES']

# Collect twitter credentials of mine
consumer_key = 'sUvyXKpgWNDh5HL25lpbUnT6K'
consumer_secret = 'C9bb39ZgYgvYGogOTq8etVglZb7BRWjgJN1RpviqwpbP23lBwR'
access_key= '1458183153344974851-cc4RVlCR0NIEUxgMyTvBZxruXx4uFC'
access_secret = 'VdR6PacH0zp0oPQgplUFIUIay3Rwf0mMRtc1DKJwPv053'

# Pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)#,wait_on_rate_limit_notify=True)

# Collect twitter posts with 6 features
for car in carmaker:
    # Create new files and save twitter posts accordingly
    file = open("Carmaker_tweets_"+car+".csv","w")
    alltweets = csv.writer(file)
    query = car + ' -filter:retweets  -filter:replies'
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en',tweet_mode = 'extended').items(500)
    for tweet in tweets:
        status = tweet._json
        created_at = status['created_at']
        tweet_id = status['id_str']
        tweet_text = status['full_text']        
        tweet_text = re.sub(r'\W',' ',tweet_text)
        number_rts = status['retweet_count']
        fave_cnt = status['favorite_count']

        try:
            alltweets.writerow([car,created_at,tweet_id, tweet_text, number_rts, fave_cnt])
        except tweepy.TweepError:
            time.sleep(120) 
file.close()

txt_files = []
for car in carmaker:
    txt_files.append("Carmaker_tweets_"+car+".csv")
print(txt_files)
