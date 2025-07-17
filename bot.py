import tweepy
import time

import tweepy.cursor
from config import API_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET,API_SECRET

#AUTH

auth = tweepy.OAuth1UserHandler(
    API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def hashtag_takibi(hashtag,count):
    print(f"for {hashtag} tweets")
    for tweet in tweepy.Cursor(api.search_tweets, hashtag, lang="tr").items(count):
        try:
            print(f"founded: @{tweet.user.screen_name} - {tweet.text}")
            time.sleep(2)    
        except Exception as e:
            print("Error❗", e)

def send_tweet(message):
    api.update_status(message)
    print("Tweet sended 🌐")
